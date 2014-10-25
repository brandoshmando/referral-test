from django.db import models
from django.utils import timezone

class Link(models.Model):
  title = models.CharField(max_length=200)
  clicks = models.IntegerField()

