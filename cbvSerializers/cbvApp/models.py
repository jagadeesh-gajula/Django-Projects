from django.db import models



# Create your models here.
class student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=10,decimal_places=3)

