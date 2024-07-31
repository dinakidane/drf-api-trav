from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('recipient__username', 'actor__username', 'verb')

