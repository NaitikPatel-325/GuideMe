# Generated by Django 5.0.2 on 2024-04-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_booking_hrs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='Guide_Profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='User_Profile'),
        ),
    ]
