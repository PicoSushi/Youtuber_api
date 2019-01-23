from rest_framework import serializers
from .models import Vtuber


class VtuberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtuber
        fields = '__all__'
