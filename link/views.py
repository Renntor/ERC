from rest_framework.response import Response
from link.models import Link
from rest_framework import generics
from link.permissions import IsUser
from link.serializers import LinkSerializers, LinkUpdateSerializers
from django_filters.rest_framework import DjangoFilterBackend


class LinkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsUser]
    serializer_class = LinkSerializers

    def update(self, request, *args, **kwargs):
        self.serializer_class = LinkUpdateSerializers
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']

    def perform_create(self, serializer):
        new_object = serializer.save()
        new_object.owner = self.request.user
        new_object.save()

