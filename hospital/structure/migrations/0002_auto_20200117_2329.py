# Generated by Django 3.0.2 on 2020-01-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='photo',
            field=models.ImageField(blank=True, upload_to='structure/cabinets/'),
        ),
    ]
