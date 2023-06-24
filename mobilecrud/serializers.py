from rest_framework import serializers
from .models import Mobile



class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id','name','company_name','price','description']
        