# Generated by Django 3.2 on 2023-07-13 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0010_auto_20230630_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiosettings',
            name='high_freq_damping_trackone',
            field=models.IntegerField(default=50, help_text='controls the damping of high frequencies', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='high_freq_damping_tracktwo',
            field=models.IntegerField(default=50, help_text='controls the damping of high frequencies', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='reverb_trackone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='reverb_tracktwo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='reverberance_trackone',
            field=models.IntegerField(default=50, help_text='controls the amount of reverb', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='audiosettings',
            name='reverberance_tracktwo',
            field=models.IntegerField(default=50, help_text='controls the amount of reverb', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='audiosettings',
            name='crossfade_duration',
            field=models.IntegerField(default=2000, help_text='Define the duration of the crossfade in milliseconds', validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='audiosettings',
            name='fade_in_duration_trackone',
            field=models.IntegerField(default=1000, help_text='in milliseconds', validators=[django.core.validators.MinValueValidator(1000.0)]),
        ),
        migrations.AlterField(
            model_name='audiosettings',
            name='fade_in_duration_tracktwo',
            field=models.IntegerField(default=1000, help_text='in milliseconds', validators=[django.core.validators.MinValueValidator(1000.0)]),
        ),
        migrations.AlterField(
            model_name='audiosettings',
            name='fade_out_duration_trackone',
            field=models.IntegerField(default=1000, help_text='in milliseconds', validators=[django.core.validators.MinValueValidator(1000.0)]),
        ),
        migrations.AlterField(
            model_name='audiosettings',
            name='fade_out_duration_tracktwo',
            field=models.IntegerField(default=1000, help_text='in milliseconds', validators=[django.core.validators.MinValueValidator(1000.0)]),
        ),
    ]