from .models import Discounts
from .serializers import DiscountsSerializer
from rest_framework import generics


class DiscountsList(generics.ListCreateAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer


class DiscountsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer
