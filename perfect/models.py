from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    image = models.ImageField(upload_to='upload/pics', default='logo.png')
