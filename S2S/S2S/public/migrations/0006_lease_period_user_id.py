# Generated by Django 2.1 on 2018-10-01 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20180910_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease_period',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]