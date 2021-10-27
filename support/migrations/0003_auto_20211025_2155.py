# Generated by Django 3.2.8 on 2021-10-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_alter_ticket_state_of_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='state_of_request',
            field=models.CharField(choices=[('Не решён', 'не решён'), ('Решён', 'решён'), ('Заморожен', 'заморожен')], default=('Не решён', 'не решён'), max_length=20),
        ),
    ]