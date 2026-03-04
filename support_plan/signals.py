from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from .models import SupportPlan, PlanHistory

@receiver(post_save, sender=SupportPlan)
def save_history(sender, instance, created, **kwargs):
    PlanHistory.objects.create(
        plan=instance,
        snapshot=model_to_dict(instance)
    )