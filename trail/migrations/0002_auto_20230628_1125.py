# Generated by Django 3.2 on 2023-06-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiosettings',
            name='normalize_trackone_target_dBFS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='normalize_tracktwo_target_dBFS',
            field=models.IntegerField(default=0),
        ),
    ]
