from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'блоги'



class Records(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    name = models.CharField(max_length=30, verbose_name='Имя')
    sum = models.IntegerField(verbose_name='Сумма')
    coment = models.CharField(max_length=80, blank=True, verbose_name='Коментарий')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Задолжность'
        verbose_name_plural = 'Задолжности'

# Create your models here.
