from rest_framework import serializers
from backend.finances.models import RefCurrency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCurrency
        fields = '__all__'