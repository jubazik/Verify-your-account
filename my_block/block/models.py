from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='event_images/')



class Records(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    sum = models.IntegerField()
    coment = models.CharField(max_length=80, blank=True)


# Create your models here.
