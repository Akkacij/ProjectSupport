# Generated by Django 3.2.8 on 2021-10-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.IntegerField(),
        ),
    ]
