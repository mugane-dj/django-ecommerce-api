# Generated by Django 4.0.4 on 2022-05-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
