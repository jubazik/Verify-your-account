# Generated by Django 4.1.5 on 2023-02-07 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_eventsblonck_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsblonck',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='events.category', verbose_name='Группа'),
            preserve_default=False,
        ),
    ]
