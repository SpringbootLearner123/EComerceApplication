from rest_framework import serializers
from .models import contactModel, ProductModel

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactModel
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
