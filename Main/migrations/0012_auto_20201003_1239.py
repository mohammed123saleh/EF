# Generated by Django 2.2.15 on 2020-10-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20200926_0341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='item',
            new_name='itemy',
        ),
    ]
