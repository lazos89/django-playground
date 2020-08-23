from django.urls import path
from .views import manufacturer_list, manufacturer_detail, product_list, product_detail

urlpatterns = [
    path("manufacturers/", manufacturer_list, name="manufacturer-list"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer-detail"),
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
]
