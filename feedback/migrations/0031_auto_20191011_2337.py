# Generated by Django 2.1.3 on 2019-10-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0030_auto_20191004_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='source_url',
            field=models.URLField(blank=True, default='', max_length=2000),
        ),
    ]
