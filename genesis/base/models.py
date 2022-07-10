from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)



class blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=100)


    
# Create your models here.
class message(models.Model):
    content = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)