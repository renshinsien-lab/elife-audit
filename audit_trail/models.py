import hashlib
import json
from django.db import models

class AuditTrail(models.Model):
    app_label = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    object_id = models.IntegerField()

    operation = models.CharField(max_length=20)  # create, update, delete
    data = models.JSONField()

    previous_hash = models.CharField(max_length=64, blank=True)
    hash = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_hash(self):
        raw = json.dumps({
            "app": self.app_label,
            "model": self.model_name,
            "id": self.object_id,
            "op": self.operation,
            "data": self.data,
            "prev": self.previous_hash,
        }, sort_keys=True, ensure_ascii=False).encode("utf-8")

        return hashlib.sha256(raw).hexdigest()

    def save(self, *args, **kwargs):
        if not self.hash:
            last = AuditTrail.objects.order_by("-id").first()
            self.previous_hash = last.hash if last else ""
            self.hash = self.calculate_hash()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["id"]