# Generated by Django 3.0.7 on 2020-06-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='latest_modified_date',
            field=models.DateTimeField(),
        ),
    ]
