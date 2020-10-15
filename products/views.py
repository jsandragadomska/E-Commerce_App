from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from .models import Product

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "home.html", {})

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404

    return HttpResponse(f"Product name: {obj.title}")

def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})

    return JsonResponse({"id": obj.id})