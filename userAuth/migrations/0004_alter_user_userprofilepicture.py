# Generated by Django 5.1.3 on 2024-12-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0003_alter_user_userprofilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userProfilePicture',
            field=models.ImageField(upload_to='userAuth/static/profilePhoto/'),
        ),
    ]
