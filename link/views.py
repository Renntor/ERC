from link.models import Link
from rest_framework import generics
from link.permissions import IsUser
from link.serializers import LinkSerializers


class LinkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsUser]
    serializer_class = LinkSerializers

class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers