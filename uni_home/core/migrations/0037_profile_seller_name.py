# Generated by Django 4.0.6 on 2023-05-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='seller_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
