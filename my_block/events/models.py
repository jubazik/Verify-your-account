from django.db import models


class Event(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    event_image = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=300)


class EventsBlonck(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='events_images/')
    test = models.TextField()
# Create your models here.
