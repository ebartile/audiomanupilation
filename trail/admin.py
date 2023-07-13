from django.contrib import admin
from .models import AudioSettings

@admin.register(AudioSettings)
class AudioSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'fadein_trackone', 'fadeout_trackone', 'fadein_tracktwo', 'fadeout_tracktwo',  'normalize_trackone', 'normalize_tracktwo', 'silence_detection', 'crossfade']
    list_filter = ['normalize_trackone', 'normalize_tracktwo']
    search_fields = ['id']

    def has_add_permission(self, request):
        # Check if there is already a record
        existing_record_count = AudioSettings.objects.count()
        if existing_record_count >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the record
        return False