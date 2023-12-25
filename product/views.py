from rest_framework.response import Response
from product.models import Product
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from product.serializers import ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [IsAdminUser]
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers