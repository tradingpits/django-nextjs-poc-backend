# Generated by Django 4.0.1 on 2022-01-24 14:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_alter_campaign_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image'),
        ),
    ]
