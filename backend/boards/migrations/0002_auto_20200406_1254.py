# Generated by Django 2.2.5 on 2020-04-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
