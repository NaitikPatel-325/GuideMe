# Generated by Django 5.0.2 on 2024-03-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_user_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('guide', 'Guide'), ('user', 'User')], default='user', max_length=20),
        ),
    ]
