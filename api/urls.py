from django.urls import path
from api.views import (CreateProductBase, ListProductsBase, UpdateProductBase,
	CreateProductEstablishment)

urlpatterns = [
	path('products/create', CreateProductBase.as_view(), name = 'create-product'),
	path('products/list', ListProductsBase.as_view(), name = 'list-products'),
	path('products/update/<int:pk>', UpdateProductBase.as_view(), name = 'update-product'),
	#path('establishment/create', CreateEstablishment.as_view(), name = 'create-establishment'),
	path('products-establishment/create', CreateProductEstablishment.as_view(), name = 'create-product-establishment'),
	#path('products-establishment/list', ListProductsEstablishment.as_view(), name = 'list-products-establishment'),
]