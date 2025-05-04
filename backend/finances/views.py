from functools import partial

from rest_framework import viewsets, status
from rest_framework.response import Response
from backend.finances.models import RefCurrency
from backend.finances.serializers import CurrencySerializer


# Create your views here.
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = RefCurrency.objects.all()
    serializer_class = CurrencySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #print('Validation errors: ', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        currency = self.get_object()
        serializer = self.get_serializer(currency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print('Validation errors: ', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)