from django.shortcuts import render, redirect
from refer_sys.models import Link
from .forms import LinkForm
def root_page(request):
  links = Link.objects.order_by("created_at")
  form = LinkForm()
  if request.method == "POST":
    form = LinkForm(request.POST)
    if form.is_valid():
      link = form.save()
      return redirect('/')
  return render (request, 'refer_sys/root_page.html',
    {'links':links, 'form':form}
    )
# def destroy_link

# def landing_page(request)


