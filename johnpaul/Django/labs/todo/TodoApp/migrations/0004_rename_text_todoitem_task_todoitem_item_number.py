# Generated by Django 4.1.4 on 2022-12-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_todoitem_date_due'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='text',
            new_name='task',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='item_number',
            field=models.IntegerField(default=0),
        ),
    ]
