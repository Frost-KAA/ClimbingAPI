from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets
from .serializers import TrainerSerializer
from .serializers import ServiceSerializer
from .serializers import LessonSerializer
from .models import Trainer
from .models import Service
from .models import Lesson

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all().order_by('name')
    serializer_class = TrainerSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('id')
    serializer_class = LessonSerializer