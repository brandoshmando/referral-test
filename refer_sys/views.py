from django.shortcuts import render

def root_page(request):
  return render (request, 'refer_sys/root_page.html', {})
