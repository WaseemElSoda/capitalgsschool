from django.contrib import admin
from .models import Message

# Register your models here.

@admin.register(Message)
class WhatsAppAdmin(admin.ModelAdmin):
    list_display = ["id", "date_sent", "communication_type"]
    list_filter = ["communication_type"]
