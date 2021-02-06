from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from .views import TestView


urlpatterns = [
    path('get_token',obtain_jwt_token),
    path('test_api',TestView.as_view())
]








