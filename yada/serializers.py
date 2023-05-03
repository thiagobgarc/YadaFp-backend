from .models import YadaFp
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class YadaFpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YadaFp
        fields = ['id', 'name', 'phone']