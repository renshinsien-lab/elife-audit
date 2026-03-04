from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.conf import settings
from .models import AuditTrail
import datetime
import json


AUDIT_TARGET_APPS = ("support_plan", "group_home")


def serialize(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    if hasattr(obj, "pk"):
        return obj.pk
    return obj


def safe_dict(instance):
    raw = model_to_dict(instance)
    return {k: serialize(v) for k, v in raw.items()}


@receiver(post_save)
def audit_save(sender, instance, created, **kwargs):
    # migration 実行中は無効
    if getattr(settings, "MIGRATING", False):
        return

    if sender._meta.app_label not in AUDIT_TARGET_APPS:
        return

    AuditTrail.objects.create(
        app_label=sender._meta.app_label,
        model_name=sender.__name__,
        object_id=instance.pk,
        operation="create" if created else "update",
        data=safe_dict(instance),
    )


@receiver(post_delete)
def audit_delete(sender, instance, **kwargs):
    if getattr(settings, "MIGRATING", False):
        return

    if sender._meta.app_label not in AUDIT_TARGET_APPS:
        return

    AuditTrail.objects.create(
        app_label=sender._meta.app_label,
        model_name=sender.__name__,
        object_id=instance.pk,
        operation="delete",
        data=safe_dict(instance),
    )