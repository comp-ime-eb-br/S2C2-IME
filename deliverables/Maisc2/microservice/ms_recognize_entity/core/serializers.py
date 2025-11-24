from rest_framework import serializers 
from .models import Recognize

class RecognizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recognize
        fields = '__all__'
