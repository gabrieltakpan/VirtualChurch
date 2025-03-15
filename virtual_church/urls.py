from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Import static helper function
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('live_event/', views.live_event, name='live_event'),
    path('resources/', views.resources, name='resources'),
    path('sermons/', views.sermon_list, name='sermon_list'),  # List view
    path('sermons/<int:pk>/', views.sermon_detail, name='sermon_detail'), 
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
