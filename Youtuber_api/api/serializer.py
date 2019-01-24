from rest_framework import serializers
from .models import Vtuber, Youtuber


class VtuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtuber
        fields = '__all__'


class YoutuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtuber
        fields = '__all__'
