# Generated by Django 2.1.3 on 2019-02-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appaccounts', '0005_auto_20190201_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='internal_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
