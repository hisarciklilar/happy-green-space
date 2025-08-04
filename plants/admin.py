from django.contrib import admin
from .models import Plant
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Plant)
class ForumAdmin(SummernoteModelAdmin):

    list_display = ('plant_name', 'owner_id', 'grew_well', 'date_planted')
    search_fields = ['plant_name', 'notes']
    list_filter = ('grew_well',)
    