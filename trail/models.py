from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AudioSettings(models.Model):
    id = models.AutoField(primary_key=True)
    reverb_trackone = models.BooleanField(default=False)
    reverb_tracktwo = models.BooleanField(default=False)
    fadein_trackone = models.BooleanField(default=False)
    fade_in_duration_trackone = models.IntegerField(
        help_text="in milliseconds",
        default=1000,
        validators=[MinValueValidator(1000.0)]
    )
    fadeout_trackone = models.BooleanField(default=False)
    fade_out_duration_trackone = models.IntegerField(
        help_text="in milliseconds",
        default=1000,
        validators=[MinValueValidator(1000.0)]
    )
    fadein_tracktwo = models.BooleanField(default=False)
    fade_in_duration_tracktwo = models.IntegerField(
        help_text="in milliseconds",
        default=1000,
        validators=[MinValueValidator(1000.0)]
    )
    fadeout_tracktwo = models.BooleanField(default=False)
    fade_out_duration_tracktwo = models.IntegerField(
        help_text="in milliseconds",
        default=1000,
        validators=[MinValueValidator(1000.0)]
    )
    normalize_trackone = models.BooleanField(default=False)
    # Headroom refers to the amount of available dynamic range or amplitude 
    # range in an audio signal before it reaches the maximum peak level. 
    # It is the difference between the maximum peak level that an audio signal 
    # can reach and the level at which it is typically mixed or mastered.
    normalize_trackone_headroom = models.DecimalField(
        default=-12.0,
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(-12.0), MaxValueValidator(-6.0)]
    )
    normalize_tracktwo = models.BooleanField(default=False)
    normalize_tracktwo_headroom = models.DecimalField(
        default=-12.0,
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(-12.0), MaxValueValidator(-6.0)]
    )
    silence_detection = models.BooleanField(default=False)
    min_silence_duration = models.IntegerField(
        help_text="Minimum duration of silence in milliseconds",
        default=1000,
        validators=[MinValueValidator(0)]
    )
    silence_threshold = models.IntegerField(
        help_text="Silence threshold in dBFS (decibels relative to full scale)",
        default=-40,
        validators=[MaxValueValidator(0)]
    )
    crossfade = models.BooleanField(default=False)
    crossfade_duration = models.IntegerField(
        help_text="Define the duration of the crossfade in milliseconds",
        default=2000,
        validators=[MinValueValidator(0)]
    )


