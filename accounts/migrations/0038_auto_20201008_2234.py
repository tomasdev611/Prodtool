# Generated by Django 2.1.3 on 2020-10-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0037_auto_20201008_1716"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="code",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
