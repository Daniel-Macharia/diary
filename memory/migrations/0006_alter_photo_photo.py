# Generated by Django 5.1.3 on 2024-12-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0005_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='memory/static/memory/'),
        ),
    ]
