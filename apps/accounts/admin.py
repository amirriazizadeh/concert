from django.contrib import admin
from .models import ProfileModel

# Register your models here.

@admin.register(ProfileModel)
class profileAdmin(admin.ModelAdmin):
    list_display=["user",]