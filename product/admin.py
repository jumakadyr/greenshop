from django.contrib import admin
from .models import Plant, Category, Tag

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


