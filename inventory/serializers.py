from rest_framework import serializers
from .models import  LguEquipment


class LguEquipmentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = LguEquipment
        fields = '__all__'
        

   