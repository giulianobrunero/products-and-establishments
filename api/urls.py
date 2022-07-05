from django.urls import path
from api.views import ListProducts

urlpatterns = [
    path('products/list', ListProducts.as_view(), name = 'list-products'),
]