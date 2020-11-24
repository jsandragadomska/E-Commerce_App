from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from products.models import Product
from .models import Order
from .forms import OrderForm

@login_required
def order_checkout_view(request):
    qs = Product.objects.filter(featured=True)
    if not qs.exists():
        return redirect("/home")
    product = qs.first()
    user = request.user
    order_id =request.session.get("order_id")
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None
    if order_id == None:
        new_creation = True
        order_obj = Order.objects.create(product=product, user=user)
    if order_obj != None and new_creation == False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product, user=user)
    request.session['order_id'] = order_obj.id
    form = OrderForm(request.POST or None, product=product)
    if form.is_valid():
        print(form.cleaned_data.get("shipping_address"))
        print(form.cleaned_data.get("billing_address"))
    return render(request, 'products/forms.html', {"form": form})