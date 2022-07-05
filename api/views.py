from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, Product, ProductEstablishment)
from api.serializers import (EstablishmentSerializer, 
	ProductSerializer, ProductEstablishmentSerializer)
from django_filters.rest_framework import DjangoFilterBackend


class CreateProduct(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ListProductsBase(generics.ListAPIView):
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
	serializer_class = ProductEstablishmentSerializer
	filter_backends = [DjangoFilterBackend]
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