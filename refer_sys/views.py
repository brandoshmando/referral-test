from django.shortcuts import render

def root_page(request):
  render (request, 'refer_sys/root_page.html', {})
