from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from .models import Product

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    return HttpResponse(f"Product name: {obj.title}")

def product_api_detail_view(request, id, *args, **kwargs):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})

    return JsonResponse({"id": obj.id})