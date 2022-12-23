from django.contrib import admin

# Register your models here.
from .models import Trainer
admin.site.register(Trainer)
from .models import Service
admin.site.register(Service)
from .models import Lesson
admin.site.register(Lesson)