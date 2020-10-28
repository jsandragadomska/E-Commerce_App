from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .forms import ProductForm
from .models import Product

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

def product_create_view(request, *args, **kwargs):
    #print(request.POST)
    #print(request.GET)
    if request.method == "POST":
        post_data = request.POST or None
        if post_data != None:
            my_form = ProductForm(request.POST)
            if my_form.is_valid():
                title_from_input = my_form.cleaned_data.get("title")
                Product.objects.create(title=title_from_input)
            print("post_data", post_data)
    return render(request, "products/forms.html", {})