# Generated by Django 3.0.4 on 2020-03-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200329_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
