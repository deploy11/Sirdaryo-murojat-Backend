from .models import *
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers

class SorovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorov
        fields = '__all__'  # Modeldagi barcha maydonlarni qo'shadi

class SorovStatisticsSerializer(serializers.Serializer):
    total_count = serializers.IntegerField()
    korish_true_count = serializers.IntegerField()
    korish_false_count = serializers.IntegerField()



