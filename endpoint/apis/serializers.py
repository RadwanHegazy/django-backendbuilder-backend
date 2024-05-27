from rest_framework import serializers
from ..models import Endpoint

class EndpointSerializer (serializers.ModelSerializer) :
    class Meta:
        model = Endpoint
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tenant'] = instance.tenant.name
        return data

