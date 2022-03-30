from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'Movies Administration'
admin.site.index_title = 'Manage the movie site'

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)