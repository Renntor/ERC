from link.models import Link
from rest_framework import generics
from link.permissions import IsUser
from link.serializers import LinkSerializers
from django_filters.rest_framework import DjangoFilterBackend


class LinkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsUser]
    serializer_class = LinkSerializers




class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


    def perform_create(self, serializer):
        new_object = serializer.save()
        new_object.owner = self.request.user
        new_object.save()

