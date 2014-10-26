from django.shortcuts import render
from refer_sys.models import Link
from .forms import LinkForm
def root_page(request):
  links = Link.objects.order_by("created_at")
  form = LinkForm()
  return render (request, 'refer_sys/root_page.html',
    {'links': links}
  )
# def link_create(request)
#   form =
