from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import relics.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('relics/', include('relics.urls')),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
