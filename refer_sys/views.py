from django.shortcuts import render
from refer_sys.models import Link
def root_page(request):
  links = Link.objects.order_by("created_at")
  return render (request, 'refer_sys/root_page.html',
    {'links': links}
  )
