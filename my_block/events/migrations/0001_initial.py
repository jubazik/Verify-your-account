# Generated by Django 3.2.12 on 2022-12-22 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1500, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('event_image', models.ImageField(upload_to='event_images/', verbose_name='Фото')),
                ('event_text', models.CharField(max_length=300, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='EventsBlonck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='events_images/', verbose_name='Фото')),
                ('test', models.TextField(verbose_name='Текст')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.category', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты',
                'ordering': ['-data'],
            },
        ),
    ]
