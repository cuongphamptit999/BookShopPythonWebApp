# Generated by Django 4.0.3 on 2022-03-29 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookitems', '0005_bookitem_aa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookitem',
            name='aa',
        ),
    ]