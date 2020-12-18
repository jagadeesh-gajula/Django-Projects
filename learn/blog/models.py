from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

