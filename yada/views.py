from django.shortcuts import render

# Create your views here.
from .models import YadaFp
from rest_framework import viewsets, permissions
from .serializers import YadaFpSerializer

class YadaFpViewSet(viewsets.ModelViewSet):
    queryset = YadaFp.objects.all()
    serializer_class = YadaFpSerializer
    permission_classes = [permissions.AllowAny]