# Generated by Django 2.2.15 on 2020-10-03 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_auto_20201003_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='vari',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.Variation'),
        ),
    ]
