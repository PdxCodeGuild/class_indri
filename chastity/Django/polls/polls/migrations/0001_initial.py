# Generated by Django 4.1.4 on 2022-12-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                        )
                        
                ),
                ('question_text', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
