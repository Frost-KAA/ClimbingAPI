from django.db import models

# Create your models here.
class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    year = models.DecimalField(max_digits=3, decimal_places=0)
    desc = models.CharField(max_length=255)
    upload = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.name

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    desc = models.CharField(max_length=255)
    date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    trainer = models.CharField(max_length=90)

    def __str__(self):
        return self.name