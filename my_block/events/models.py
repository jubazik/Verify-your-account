from django.db import models


class Event(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    event_image = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=300)
    def __str__(self):
        return self.event_text
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'




class EventsBlonck(models.Model):
    data = models.DateTimeField(auto_now_add=True,verbose_name='Дата')
    name = models.CharField(max_length=30,verbose_name='Имя')
    image = models.ImageField(upload_to='events_images/',verbose_name='Фото')
    test = models.TextField(verbose_name='Текст')


    def __str__(self):
        return self.name
# Create your models here.
    class  Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ['-data']
