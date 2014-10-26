from django.shortcuts import render, redirect, get_object_or_404
from refer_sys.models import Link
from .forms import LinkForm, DeleteLinkForm

def root_page(request):
  links = Link.objects.order_by("created_at")
  form = LinkForm()
  if request.method == "POST":
    form = LinkForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  return render (request, 'refer_sys/root_page.html',
    {'links':links, 'form':form}
    )

def edit_link(request, pk):
  link = get_object_or_404(Link, pk=pk)
  form = LinkForm(instance=link)

  if request.method == "POST":
    form = LinkForm(request.POST, instance=link)
    if form.is_valid():
      form.save()
      return redirect('/')
  return render(request, 'refer_sys/edit_link.html', {'form': form})

def delete_link(request, pk):
  link = get_object_or_404(Link, pk=pk)
  form = DeleteLinkForm(instance=link)
  if request.method == "POST":
    form = DeleteLinkForm(request.POST, instance=link)
    if form.is_valid():
      link.delete()
      return redirect('/')
  return render (request, 'refer_sys/root_page.html',
    {'links':links, 'form':form}
    )