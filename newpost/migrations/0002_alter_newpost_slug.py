# Generated by Django 4.2.16 on 2024-10-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]