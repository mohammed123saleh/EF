# Generated by Django 2.2.15 on 2020-11-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0066_auto_20201124_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'ordering': ['Title']},
        ),
    ]