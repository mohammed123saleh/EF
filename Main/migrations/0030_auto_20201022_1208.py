# Generated by Django 2.2.15 on 2020-10-22 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0029_auto_20201021_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='variations',
            new_name='variation',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='title',
        ),
    ]