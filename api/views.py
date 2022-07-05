from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, ProductBase, ProductEstablishment)
from api.serializers import (EstablishmentSerializer, 
	ProductBaseSerializer, ProductEstablishmentSerializer)


class CreateProductBase(generics.CreateAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


class ListProductsBase(generics.ListAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


class UpdateProductBase(generics.RetrieveUpdateAPIView):
	queryset = ProductBase.objects.all()
	serializer_class = ProductBaseSerializer


'''
class DeleteProductBase(generics.DestroyAPIView):
    queryset = ProductBase.objects.all()
    serializer_class = ProductBaseSerializer
'''
#class ListProductsEstablishments(generics.ListAPIView)


class CreateProductEstablishment(generics.ListCreateAPIView):
	queryset = ProductEstablishment.objects.all()
	serializer_class = ProductEstablishmentSerializer


class CreateEstablishment(generics.CreateAPIView):
	queryset = Establishment.objects.all()
	serializer_class = EstablishmentSerializer