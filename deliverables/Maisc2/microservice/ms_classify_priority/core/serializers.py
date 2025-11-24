from rest_framework import serializers 
from .models import Classify

class ClassifySerializers(serializers.ModelSerializer):
    class Meta:
        model = Classify
        fields = '__all__'
