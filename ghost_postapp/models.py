from django.db import models
from django.utils import timezone


class GhostInput(models.Model):
    boast_or_roast = models.BooleanField(default=False)
    post = models.CharField(max_length=500)
    up_votes = models.IntegerField(default=0, blank=True, null=True)
    down_votes = models.IntegerField(default=0, blank=True, null=True)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post
