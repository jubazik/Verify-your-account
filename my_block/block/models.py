from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='event_images/')


# Create your models here.
