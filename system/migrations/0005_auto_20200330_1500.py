# Generated by Django 3.0.4 on 2020-03-30 15:00

from django.db import migrations, models
import system.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20200330_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(validators=[system.models.validate_date]),
        ),
    ]
