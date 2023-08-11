from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.defaults import (bad_request,
                                   permission_denied,
                                   page_not_found,
                                   server_error)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='core'),
]

handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
