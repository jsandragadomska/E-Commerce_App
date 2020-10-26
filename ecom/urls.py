from django.contrib import admin
from django.urls import path, re_path
from products.views import (
    search_view,
    product_detail_view,
    product_api_detail_view,
    product_list_view,
    product_create_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_view),
    path('products/', product_list_view),
    path('products/<int:pk>/', product_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view), 
    path('products/create/', product_create_view),  
]
