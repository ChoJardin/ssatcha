# Generated by Django 3.2.3 on 2021-05-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210521_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(null=True, to='movies.Genre'),
        ),
    ]
