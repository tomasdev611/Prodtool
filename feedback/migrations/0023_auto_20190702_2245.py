# Generated by Django 2.1.3 on 2019-07-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0022_add_refresh_token_to_cfis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerfeedbackimportersettings',
            name='account_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
