from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('account/',include('account.urls')),
    path('sendc2/', include('sendc2.urls')),
    path('room/', include('room.urls')),
    path('api/', include('api.urls')),
    path('tasks/', include('tasks.urls')),
    path('statistic/', include('statistic.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

