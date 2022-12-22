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
        ordering = ['-date']


class Records(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    name = models.ForeignKey('Сounterparties', on_delete=models.PROTECT, verbose_name='Имя')
    sum = models.IntegerField(verbose_name='Сумма')
    coment = models.CharField(max_length=80, blank=True, verbose_name='Коментарий')

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Задолжность'
        verbose_name_plural = 'Задолжности'
        ordering = ['-data']


# Create your models here.
class Сounterparties(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя')
    image = models.ImageField(upload_to='event_images/', blank=True)
    surname = models.CharField(max_length=150, db_index=True, verbose_name='Фамилия')
    firma = models.CharField(max_length=150, db_index=True, verbose_name='Организация')
    phone = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Группа")
    def __str__(self):
        return f"{self.name} {self.surname} "

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ['-date']
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,verbose_name='Группа')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
