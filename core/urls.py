from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core.views import home, login_view, logout_view

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('movies/', include('movies.urls', namespace='movies')),
    path('users/', include('users.urls', namespace='users')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

admin.site.site_header = 'Movies Administration'
admin.site.index_title = 'Manage the movie site'

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)