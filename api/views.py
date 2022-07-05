from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, Product, ProductEstablishment)
from api.serializers import (EstablishmentSerializer, 
	ProductSerializer, ProductEstablishmentSerializer, ReadProductEstablishmentSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CreateProduct(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ListProducts(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class UpdateProduct(generics.RetrieveUpdateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class CreateProductEstablishment(generics.CreateAPIView):
	queryset = ProductEstablishment.objects.all()
	serializer_class = ProductEstablishmentSerializer


class CreateEstablishment(generics.CreateAPIView):
	queryset = Establishment.objects.all()
	serializer_class = EstablishmentSerializer


class ListEstablishments(generics.ListAPIView):
	queryset = Establishment.objects.all()
	serializer_class = EstablishmentSerializer


class ListProductsEstablishment(generics.ListAPIView):
	queryset = ProductEstablishment.objects.all()
	serializer_class = ReadProductEstablishmentSerializer
	filter_backends = [DjangoFilterBackend,  filters.OrderingFilter]
	filterset_fields = {
		# Product
		'product__name': ['contains'],
		'product__calories': ['gte', 'lte'],
		'product__saturated_fat_percent': ['gte', 'lte'],
		'product__sugar_percent': ['gte', 'lte'],
		# Establishment
		'establishment__name': ['contains'],
		# Product in Establishment
		'price': ['gte', 'lte']
	}
	ordering_fields = ['pk', 'price', 'product__calories', 
	'product__saturated_fat_percent', 'product__sugar_percent']
	ordering = ['price']