# Generated by Django 5.1.3 on 2024-12-11 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuth.user'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]