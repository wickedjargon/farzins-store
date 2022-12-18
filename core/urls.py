from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # admin url
    path('', include('store.urls')), # store app
    path('urls/', include('cart.urls')), # cart app
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)