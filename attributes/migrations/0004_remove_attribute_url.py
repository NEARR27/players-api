# Generated by Django 3.1.3 on 2023-05-08 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0003_attribute_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='url',
        ),
    ]