# Generated by Django 5.1.3 on 2024-12-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0002_alter_day_userid_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='memory/static/memory'),
        ),
    ]