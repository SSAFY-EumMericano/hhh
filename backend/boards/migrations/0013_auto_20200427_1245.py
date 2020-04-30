# Generated by Django 2.2.5 on 2020-04-27 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200421_0402'),
        ('boards', '0012_auto_20200427_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='isLocation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='board',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Location'),
        ),
        migrations.AddField(
            model_name='board',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DiningStore'),
        ),
    ]
