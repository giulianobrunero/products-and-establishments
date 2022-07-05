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


class ReadProductEstablishmentSerializer(serializers.ModelSerializer):
	product_name = serializers.ReadOnlyField(source='product.name')
	calories = serializers.ReadOnlyField(source='product.calories')
	saturated_fat_percent = serializers.ReadOnlyField(source='product.saturated_fat_percent')
	sugar_percent = serializers.ReadOnlyField(source='product.sugar_percent')
	establishment_name = serializers.ReadOnlyField(source='establishment.name')
	class Meta:
		model = ProductEstablishment
		fields = ['product_name', 'calories', 'saturated_fat_percent',
		'sugar_percent', 'price', 'quantity', 'establishment_name']