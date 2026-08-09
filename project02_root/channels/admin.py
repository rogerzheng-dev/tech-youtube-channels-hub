from django.contrib import admin
from .models import Channel
# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator_name', 'category', 'subscribers')
    search_fields = ('name', 'creator_name')
    ordering = ('name',)