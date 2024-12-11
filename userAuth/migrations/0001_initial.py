# Generated by Django 5.1.3 on 2024-12-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userProfilePicture', models.ImageField(upload_to='static/profilePhoto/')),
                ('userName', models.CharField(max_length=20)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userPassword', models.CharField(max_length=30)),
            ],
        ),
    ]