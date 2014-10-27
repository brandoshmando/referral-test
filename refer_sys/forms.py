from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
  class Meta:
    model = Link
    fields = ('title',)
    def clean_name(self):
        return self.cleaned_data["title"].lower()

class DeleteLinkForm(forms.ModelForm):
  class Meta:
    model = Link
    fields = []