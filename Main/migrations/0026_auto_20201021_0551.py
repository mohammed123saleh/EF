# Generated by Django 2.2.15 on 2020-10-21 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0025_remove_variation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='variations',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrItVa', to='Main.Variation'),
        ),
    ]
