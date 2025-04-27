from django.shortcuts import render
from rest_framework import viewsets
from finances.models import RefCurrency
from finances.serializers import CurrencySerializer


# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = RefCurrency.objects.all()
    serializer_class = CurrencySerializer