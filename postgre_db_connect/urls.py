from django.urls import path, include
from .views import RootPage, Connect


urlpatterns = [
    path('', RootPage.as_view(), name='root'),
    path('db-user/', Connect.as_view(), name='all_user'),
    path('db-user/<int:pk>', Connect.as_view(), name='single_user'),
]
