from django.db import models
from django.utils import timezone

class Link(models.Model):
  title = models.CharField(max_length=200, unique=True)
  clicks = models.IntegerField(default=0)
  created_at = models.DateTimeField(default=timezone.now)

  def add_click(self):
    self.clicks += 1
    self.save()

  def format_query(self):
    query = self.title.lower().split(' ')
    return "+".join(query)

