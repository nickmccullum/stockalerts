# Generated by Django 4.0.5 on 2022-06-12 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
