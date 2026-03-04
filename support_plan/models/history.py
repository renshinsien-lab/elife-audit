from django.db import models
from .plan import SupportPlan

class PlanHistory(models.Model):
    plan = models.ForeignKey(SupportPlan, related_name="histories", on_delete=models.CASCADE)
    snapshot = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)