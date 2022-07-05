from django.urls import path
from api.views import (CreateProduct, ListProducts, UpdateProduct,
	CreateProductEstablishment, CreateEstablishment, ListEstablishments, ListProductsEstablishment)

urlpatterns = [
	path('products/create', CreateProduct.as_view(), name = 'create-product'),
	path('products/list', ListProducts.as_view(), name = 'list-products'),
	path('products/update/<int:pk>', UpdateProduct.as_view(), name = 'update-product'),
	path('establishment/create', CreateEstablishment.as_view(), name = 'create-establishment'),
	path('establishment/list', ListEstablishments.as_view(), name = 'list-establishments'),
	path('products-establishment/create', CreateProductEstablishment.as_view(), name = 'create-product-establishment'),
	path('products-establishment/list', ListProductsEstablishment.as_view(), name = 'list-products-establishment'),
]