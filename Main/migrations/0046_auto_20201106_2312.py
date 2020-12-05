# Generated by Django 2.2.15 on 2020-11-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0045_auto_20201106_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_category',
            field=models.CharField(choices=[('T', 'Towels'), ('BS', 'Bedsheets'), ('V', 'Variety'), ('PC', 'Pillowcases')], default='V', help_text='Products Dropdown in Egypt Fabrics Navbar', max_length=2, verbose_name='2-Product Category'),
        ),
    ]
