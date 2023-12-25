from rest_framework import serializers

from link.models import Link


class LinkSerializers(serializers.ModelSerializer):



    class Meta:
        model = Link
        exclude = ('owner',)
