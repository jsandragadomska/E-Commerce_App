from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ProductModelForm
from .models import Product

def home_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=[0])
    print(query, qs)
    context = {"name": "Sandra", "query": query}
    return render(request, "home.html", context)

def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=[0])
    print(query, qs)
    context = {"name": "Sandra", "query": query}
    return render(request, "home.html", context)

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404

    # return HttpResponse(f"Product name: {obj.title}")
    return render(request, "products/detail.html", {"object": obj})

def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})

    return JsonResponse({"id": obj.id})

def product_list_view(request, *args, **kwargs):
    # qs = query set
    qs = Product.objects.all()
    context = {"object_list": qs}

    return render(request, "products/list.html", context)

@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductModelForm()
    return render(request, "products/forms.html", {"form": form})