# Generated by Django 3.2.19 on 2023-09-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraurant_activities_management', '0002_auto_20230928_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
