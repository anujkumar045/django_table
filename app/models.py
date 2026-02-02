from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=40)
    Gender=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=30)
    Profile_picture=models.ImageField(upload_to='image')
    Music=models.FileField(upload_to='audio')
    Video=models.FileField(upload_to='video')
    Resume=models.FileField(upload_to='doc')
    

