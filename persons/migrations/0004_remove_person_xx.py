# Generated by Django 4.0.3 on 2022-03-29 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_person_xx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='xx',
        ),
    ]
