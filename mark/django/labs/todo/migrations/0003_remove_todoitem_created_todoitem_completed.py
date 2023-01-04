# Generated by Django 4.1.4 on 2022-12-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='created',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.DateTimeField(null=True),
        ),
    ]