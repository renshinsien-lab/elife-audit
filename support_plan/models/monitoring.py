from django.db import models
from .plan import SupportPlan

class Monitoring(models.Model):
    plan = models.ForeignKey(SupportPlan, related_name="monitorings", on_delete=models.CASCADE)

    date = models.DateField()
    result = models.TextField()
    evaluation = models.TextField()
    revised_content = models.TextField(blank=True)