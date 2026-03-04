from django.db import models
from .plan import SupportPlan
from group_home.models.master import UserProfile

class SupportItem(models.Model):
    plan = models.ForeignKey(SupportPlan, related_name="items", on_delete=models.CASCADE)

    goal = models.TextField()
    content = models.TextField()
    evaluation_time = models.CharField(max_length=100)
    staff = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)