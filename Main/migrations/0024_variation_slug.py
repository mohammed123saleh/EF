# Generated by Django 2.2.15 on 2020-10-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0023_delete_mat'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='slug',
            field=models.SlugField(blank=True, help_text='random input', max_length=300, null=True, unique=True),
        ),
    ]