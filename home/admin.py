from django.contrib import admin
from .models import LiveStream, Sermon, Donation, Resource


admin.site.register(LiveStream)
admin.site.register(Sermon)
admin.site.register(Donation)
admin.site.register(Resource)

admin.site.site_header = 'Virtual Church Administration Page'
