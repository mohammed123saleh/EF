# Generated by Django 2.2.15 on 2020-11-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0055_auto_20201118_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, help_text='this field is optional', null=True, upload_to='Egypt_fabrics', verbose_name='2- image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, help_text='this field is optional', null=True, upload_to='Egypt_fabrics', verbose_name='3- image'),
        ),
    ]
