from django.contrib import admin
from .models import EventType, Event
from django.utils.safestring import mark_safe
from .models import Event

admin.site.register(EventType)
admin.site.register(Event)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status', 'whatsapp_share_link')

    def whatsapp_share_link(self, obj):
        from django.contrib.sites.models import Site
        from urllib.parse import quote

        current_site = Site.objects.get_current()
        event_url = f"https://{current_site.domain}{obj.get_absolute_url()}"
        message = f"Check out this event: {obj.title}\n{event_url}"
        url = f"https://wa.me/?text={quote(message)}"
        return mark_safe(f'<a href="{url}" target="_blank">Share on WhatsApp</a>')

    whatsapp_share_link.short_description = "WhatsApp Share"
