# Generated by Django 3.0.3 on 2020-05-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.RemoveField(
            model_name='cook',
            name='img',
        ),
        migrations.RemoveField(
            model_name='cook',
            name='urlField',
        ),
    ]