from django.db import models
from .base import TimeStampedModel
from group_home.models.master import Resident, UserProfile

class SupportPlan(TimeStampedModel):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)

    overall_policy = models.TextField()
    long_term_goal = models.TextField()
    short_term_goal = models.TextField()

    next_monitoring_date = models.DateField(null=True, blank=True)

    revision = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]