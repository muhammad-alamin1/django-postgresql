from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('postgre_db_connect.urls'), name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('postgre_db_connect.urls'), name='db_data_api'),
    path('api/orm/', include('orm_test.urls'), name='orm_test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
