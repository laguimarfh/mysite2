# Generated by Django 3.1.1 on 2020-10-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, help_text='The date & time this article was published', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The date & time this article was published', null=True, unique_for_date='published'),
        ),
    ]