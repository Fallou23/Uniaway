# Generated by Django 4.0.6 on 2023-02-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blank_profile.jpg', upload_to='post_images'),
        ),
    ]
