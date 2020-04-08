from rest_framework import serializers
from .models import District, City

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        exclude = ('count', ) 
        ref_name = '지역구'

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        
        fields = "__all__"
        depth = 1
        ref_name = '행정구역, 주소'
