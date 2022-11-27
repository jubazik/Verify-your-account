from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField()
    text = models.TextField
    image = models.ImageField(upload_to='event_images/')


# Create your models here.
