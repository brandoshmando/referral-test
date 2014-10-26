from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
  class Meta:
    model = Link
    fields = ('title',)

class DeleteLinkForm(forms.ModelForm):
  class Meta:
    model = Link
    fields = []