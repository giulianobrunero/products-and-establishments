from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, ProductBase, Product)
from api.serializers import (EstablishmentSerializer, 
	ProductBaseSerializer, ProductSerializer)


class CreateProductBase(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		data = {
			'name': request.data.get('name'),
			'code': request.data.get('code'),
			'brand': request.data.get('brand'),
			'product_type': request.data.get('product_type'),
			'calories': request.data.get('calories'),
			'saturated_fat_percent': request.data.get('saturated_fat_percent'),
			'sugar_percent': request.data.get('sugar_percent'),
			'description': request.data.get('description')
		}
		serializer = ProductBaseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProductsBase(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		products_base = ProductBase.objects.all()
		serializer = ProductBaseSerializer(products_base, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)




class ListProducts(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProduct(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request, *args, **kwargs):
		data = {
			'product_base': request.data.get('product_base_id'),
			'establishment': request.data.get('establishment_id'),
			'price': request.data.get('price'),
			'quantity': request.data.get('quantity')
		}
		serializer = ProductSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




