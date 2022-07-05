from rest_framework import serializers

from api.models import (Establishment, ProductBase, ProductEstablishment)

class EstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Establishment
		fields = '__all__'


class ProductBaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductBase
		fields = '__all__'


class ProductEstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductEstablishment
		fields = '__all__'
