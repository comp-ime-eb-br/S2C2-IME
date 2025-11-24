from rest_framework import serializers 
from .models import Delivery

class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
