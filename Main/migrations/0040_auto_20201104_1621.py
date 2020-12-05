# Generated by Django 2.2.15 on 2020-11-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0039_auto_20201104_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('Si', 'Single 120 x 200'), ('Q', 'Queen 160 x 200'), ('K', 'King 180 x 200'), ('SK', 'Super King 200 x 200'), ('S', 'Set'), ('PS', 'pillow:Standard  51 x 56'), ('PQ', 'pillow: Queen size  51 x 76'), ('PK', 'pillow: King size  51 x 92'), ('PB', 'pillow: Body size  51 x 137 ')], default='S', max_length=2, null=True),
        ),
    ]
