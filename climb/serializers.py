# serializers.py
from rest_framework import serializers

from .models import Trainer
from .models import Lesson
from .models import Service

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ('id', 'name', 'year', 'desc', 'upload')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price', 'desc')

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'desc', 'date', 'time', 'trainer')