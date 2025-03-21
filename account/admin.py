from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id",'username', "first_name", 'last_name', "email")
    list_display_links = ('id', 'username',"first_name", 'last_name')
    search_fields = ('first_name', 'username','last_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
