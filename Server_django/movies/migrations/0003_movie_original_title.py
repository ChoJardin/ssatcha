# Generated by Django 3.2.3 on 2021-05-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='original_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]