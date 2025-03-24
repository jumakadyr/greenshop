from django.contrib import admin
from .models import Plant, Category, Tag, PlantImage


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)

@admin.register(Category)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class PlantCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(PlantImage)
class PlantTagAdmin(admin.ModelAdmin):
    pass
