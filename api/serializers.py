from rest_framework import serializers

from api.models import (Establishment, ProductBase, Product)

class EstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Establishment
		fields = '__all__'


class ProductBaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductBase
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'
