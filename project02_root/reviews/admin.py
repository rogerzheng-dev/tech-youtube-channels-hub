from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('channel', 'user', 'rating', 'created_at')
    search_fields = ('channel__name', 'user__username')
    ordering = ('-created_at',)