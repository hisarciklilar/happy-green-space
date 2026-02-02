from django.contrib import admin
from .models import Plant, GardenPlot, PlantLog, WishList, ToDoItem


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'category', 'suggested_by', 'created_on')
    search_fields = ['name', 'scientific_name', 'description']
    list_filter = ('category',)


@admin.register(GardenPlot)
class GardenPlotAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_on')
    search_fields = ['name', 'description']
    list_filter = ('owner',)


@admin.register(PlantLog)
class PlantLogAdmin(admin.ModelAdmin):
    list_display = ('plant', 'owner', 'plot', 'status', 'date_planted', 'date_harvested')
    search_fields = ['plant__name', 'notes']
    list_filter = ('status', 'owner')


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('plant', 'owner', 'target_season', 'created_on')
    search_fields = ['plant__name', 'notes']
    list_filter = ('target_season', 'owner')


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'plant', 'plot', 'priority', 'due_date', 'completed')
    search_fields = ['title']
    list_filter = ('completed', 'priority', 'owner')
