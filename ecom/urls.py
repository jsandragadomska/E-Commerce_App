from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from products.views import (
    home_view,
    search_view,
    product_detail_view,
    product_api_detail_view,
    product_list_view,
    product_create_view,
)
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home_view'),
    path('search/', search_view, name='search_view'),
    path('products/', product_list_view, name='product_list_view'),
    path('products/<int:pk>/', product_detail_view, name='product_detail_view'),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view, name='product_api_detail_view'), 
    path('products/create/', product_create_view, name='product_create_view'),

    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),
]