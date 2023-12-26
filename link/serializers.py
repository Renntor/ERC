from rest_framework import serializers

from link.models import Link


class LinkSerializers(serializers.ModelSerializer):

    def validate(self, data):
        if (data.get('structure', None) == 'FC') and (data.get('supplier', None) is not None):
            raise serializers.ValidationError(
                "the factory can't have a supplier"
            )
        elif data.get('structure', None) in ['IE', 'RN'] and (data.get('supplier', None) is None):
            raise serializers.ValidationError(
                "for IE and RN the supplier field must be filled in"
            )
        return data

    class Meta:
        model = Link
        exclude = ('owner',)
