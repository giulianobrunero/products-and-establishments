from rest_framework import serializers

from api.models import (Establishment, Product, ProductEstablishment)

class EstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Establishment
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class ProductEstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductEstablishment
		fields = '__all__'
