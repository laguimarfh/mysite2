# Generated by Django 3.1.1 on 2020-10-05 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20201004_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='post',
        ),
    ]