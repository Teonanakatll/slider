# Generated by Django 5.0.1 on 2024-01-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_app', '0005_slideritem'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideritem',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]