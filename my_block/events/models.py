from django.db import models

"""
Здесь записна все модели  Event, EventBlonck, Caterory
"""
class Event(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    event_image = models.ImageField(upload_to='event_images/', verbose_name='Фото')
    event_text = models.CharField(max_length=300, verbose_name='Текст')

    def __str__(self):
        return self.event_text

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-data']

"""


"""
class EventsBlonck(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    name = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(upload_to='events_images/', blank=True , verbose_name='Фото')
    test = models.TextField(verbose_name='Текст')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Группа')

    def my_func(self):
        return 'hello word'
    def __str__(self):
        return self.name

    # Create your models here.
    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ['-data']


class Category(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Группа')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']