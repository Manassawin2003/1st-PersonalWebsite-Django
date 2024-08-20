from django.contrib import admin
from .models import Profile, Addnewfield

class ProfileFieldInline(admin.TabularInline):
    model = Addnewfield
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'location')
    search_fields = ('name', 'email')
    inlines = [ProfileFieldInline]

@admin.register(Addnewfield)
class ProfileFieldAdmin(admin.ModelAdmin):
    list_display = ('profile', 'key')
