# Generated by Django 4.1.4 on 2022-12-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
