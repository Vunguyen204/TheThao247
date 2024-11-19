# Generated by Django 5.1.1 on 2024-11-18 14:26

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportNews', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default='No content'),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='articles/'),
        ),
    ]