# Generated by Django 2.1.3 on 2018-11-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20181128_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='snooze_till',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
