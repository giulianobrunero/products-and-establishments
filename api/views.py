from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import (Establishment, ProductBase, Product)
from api.serializers import (EstablishmentSerializer, 
	ProductBaseSerializer, ProductSerializer)

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

#class CreateProduct(generics.CreateAPIView)
#class ListProductsEstablishments(generics.ListAPIView)
