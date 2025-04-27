from rest_framework import viewsets
from backend.finances.models import RefCurrency
from backend.finances.serializers import CurrencySerializer


# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = RefCurrency.objects.all()
    serializer_class = CurrencySerializer