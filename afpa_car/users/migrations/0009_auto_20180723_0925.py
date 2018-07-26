# Generated by Django 2.0.5 on 2018-07-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_privatedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='car_owner',
            field=models.BooleanField(default=False, verbose_name="propriétaire d'un véhicule"),
        ),
        migrations.AddField(
            model_name='user',
            name='trainee',
            field=models.BooleanField(default=False, verbose_name='stagiaire'),
        ),
        migrations.AlterField(
            model_name='user',
            name='driver_license',
            field=models.BooleanField(default=False, verbose_name='permis'),
        ),
    ]