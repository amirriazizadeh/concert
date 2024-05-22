from django.contrib import admin
from apps.ticketSales.models import concertModel,locationModel,timeModel,ticketModel
# Register your models here.
@admin.register(concertModel)
class concertAdmin(admin.ModelAdmin):
    list_display=["Name","SingerName","lenght"]

@admin.register(locationModel)
class locationAdmin(admin.ModelAdmin):
    list_display=["Name","Address","Phone"]

@admin.register(timeModel)
class timeAdmin(admin.ModelAdmin):
    list_display=["Status"]

@admin.register(ticketModel)
class ticketAdmin(admin.ModelAdmin):
    list_display=["Name","Price"]