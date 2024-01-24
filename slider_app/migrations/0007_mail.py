# Generated by Django 5.0.1 on 2024-01-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_app', '0006_slideritem_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]