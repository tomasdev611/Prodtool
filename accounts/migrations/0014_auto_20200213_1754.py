# Generated by Django 2.1.3 on 2020-02-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20191004_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(choices=[('plan_Ek0Ns9AhiBtR1o', 'Early Adopter - $20/user per month'), ('plan_Gh1UcIDLlkqntF', 'Small - $49/user per month'), ('plan_Gh1Tct1NT6ncGK', 'Medium - $99/user per month')], max_length=255),
        ),
    ]
