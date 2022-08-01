from distutils.command import upload
from django.db import models

# Create your models here.
class plots(models.Model):
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    price = models.FloatField()
    bath = models.IntegerField()
    bed = models.IntegerField()
    area = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    picture=models.ImageField(upload_to="plotImages")


class agents(models.Model):
    name = models.CharField(max_length=100)   
    picture=models.ImageField(upload_to="agentImages")

class clients(models.Model):
    name = models.CharField(max_length=100)   
    picture=models.ImageField(upload_to="clientImages")
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)


class blogs(models.Model):
    name = models.CharField(max_length=100)   
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    picture=models.ImageField(upload_to="blogImages")

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class stats(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    sale = models.IntegerField()