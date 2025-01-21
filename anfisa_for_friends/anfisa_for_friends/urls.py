from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('about/', include('about.urls', namespace='about')),
    path('ice_cream/', include('ice_cream.urls', namespace='ice_cream')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
