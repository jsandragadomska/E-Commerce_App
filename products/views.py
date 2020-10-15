from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from .models import Product

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    context = {"name": "Sandra"}
    return render(request, "home.html", context)

def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404

    # print(dir(request))

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