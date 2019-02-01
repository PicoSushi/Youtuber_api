from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Vtuber, Youtuber
from .serializer import VtuberSerializer, YoutuberSerializer
import django_filters


class VtuberViewSet(viewsets.ModelViewSet):
    queryset = Vtuber.objects.all()
    serializer_class = VtuberSerializer
    # api/vtuber?tag=でtag検索対応
    filter_fields = ('name', 'tag', 'belong')


class YoutuberViewSet(viewsets.ModelViewSet):
    queryset = Youtuber.objects.all()
    serializer_class = YoutuberSerializer
    filter_fields = ('name', 'tag', 'belong')
