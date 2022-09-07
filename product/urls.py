from django.urls import path, include

from .views import (
    productlist,
)

app_name = "product"

urlpatterns = [
    path("", productlist, name= "product-list"),
    
]
