# Generated by Django 2.0 on 2020-04-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20200401_1440'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cooptype',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='cooptype',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
