# Generated by Django 3.1.1 on 2020-10-04 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201003_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique_for_date='published'),
        ),
    ]
