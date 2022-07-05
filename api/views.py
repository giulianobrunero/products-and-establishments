from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, ProductBase, ProductEstablishment)
from api.serializers import (EstablishmentSerializer, 
	ProductBaseSerializer, ProductEstablishmentSerializer)
from django_filters.rest_framework import DjangoFilterBackend


class CreateProductBase(generics.CreateAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


class ListProductsBase(generics.ListAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


class UpdateProductBase(generics.RetrieveUpdateAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


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
		'product_base__name': ['contains'],
		'product_base__calories': ['gte', 'lte'],
		'product_base__saturated_fat_percent': ['gte', 'lte'],
		'product_base__sugar_percent': ['gte', 'lte'],
		# Establishment
		'establishment__name': ['contains'],
		# Product in Establishment
		'price': ['gte', 'lte']
	}