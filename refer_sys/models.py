from django.db import models
from django.utils import timezone

class Link(models.Model):
  title = models.CharField(max_length=200, unique=True)
  clicks = models.IntegerField(default=0)
  created_at = models.DateTimeField(default=timezone.now)


