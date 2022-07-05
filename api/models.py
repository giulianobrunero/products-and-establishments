from django.db import models


class Establishment(models.Model):
	name = models.CharField(max_length=140, null=False, blank=False)
	code = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=200, null=False, blank=False)
	opening_hours = models.CharField(max_length=140, null=False, blank=False)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return f'{self.name} | {self.code}'


class ProductBase(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	code = models.CharField(max_length=20, null=True, blank=True)
	brand = models.CharField(max_length=100, null=False, blank=False)
	product_type = models.CharField(max_length=100, null=False, blank=False)
	calories = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)
	saturated_fat_percent = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)
	sugar_percent = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return f'{self.name} | {self.code}'


class Product(models.Model):
	product_base = models.ForeignKey(ProductBase,
		null=False,
		blank=False,
		verbose_name="ProductBase",
		on_delete=models.CASCADE)
	establishment = models.ForeignKey(Establishment,
		null=False,
		blank=False,
		verbose_name="Establishment",
		on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
	quantity = models.PositiveBigIntegerField(null=False, blank=False)