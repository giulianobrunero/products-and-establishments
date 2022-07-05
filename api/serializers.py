from rest_framework import serializers

from api.models import (Establishment, ProductBase, Product)

class EstablishmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Establishment
		fields = [
			'name',
			'code',
			'address',
			'opening_hours',
			'description'
		]


class ProductBaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductBase
		fields = [
			'name',
			'code',
			'brand',
			'product_type',
			'calories',
			'saturated_fat_percent',
			'sugar_percent',
			'description'
		]


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = [
			'product_base',
			'establishment',
			'price',
			'quantity'
		]
