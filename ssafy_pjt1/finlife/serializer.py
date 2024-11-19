
from rest_framework import serializers
from .models import DepositProducts, DepositOptions,Change

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepositProducts
        fields='__all__'
    # class OptionListSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model=DepositOptions
    #         fields='__all__'
    # options=OptionListSerializer(many=True, read_only=True)

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepositOptions
        fields='__all__'
        read_only_fields=('product',)

class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Change
        fields='__all__'