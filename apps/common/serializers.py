# -*- coding: utf-8 -*-
from rest_framework import exceptions, serializers


class InvalidFieldsMixin(serializers.Serializer):
    """
    Does not allow to update the fields of the list invalid_fields.
    """

    error_message = {"invalid_fields": "You cannot edit the fields: {}"}

    def validate_invalid_fields(self):
        invalid_fields = self.Meta.invalid_fields
        data = self.context.get("request").data
        fields = set(data.keys()) & set(invalid_fields)
        if fields:
            raise exceptions.ParseError(
                {
                    "invalid_fields": self.error_message["invalid_fields"].format(
                        ", ".join(list(fields))
                    )
                }
            )

    def update(self, instance, validated_data):
        self.validate_invalid_fields()
        return super(InvalidFieldsMixin, self).update(instance, validated_data)

    class Meta:
        # This list contains the fields that can not be updated.
        invalid_fields = []
