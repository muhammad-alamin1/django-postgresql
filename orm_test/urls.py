from django.urls import path, include
from .views import ORM_TEST


urlpatterns = [
    path('user/', ORM_TEST.as_view(), name='user'),
    path('user/<int:pk>', ORM_TEST.as_view(), name='single_user'),
]

