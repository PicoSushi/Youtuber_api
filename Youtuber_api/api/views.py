from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Vtuber
from .serializer import VtuberSerializer
import django_filters


class VtuberViewSet(viewsets.ModelViewSet):
    queryset = Vtuber.objects.all()
    serializer_class = VtuberSerializer
