# Generated by Django 5.0.7 on 2024-08-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='momento',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
