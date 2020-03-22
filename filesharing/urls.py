from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fileshare/',include('fileshare.urls')),
    path('account/', include('account.urls')),
    path('home/', include('home.urls')),
    path('oauth/',include('social_django.urls',namespace="social")),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
