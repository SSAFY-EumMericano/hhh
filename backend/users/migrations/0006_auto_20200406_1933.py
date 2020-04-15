# Generated by Django 2.2.5 on 2020-04-06 10:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followed',
            field=models.ManyToManyField(related_name='_user_followed_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]