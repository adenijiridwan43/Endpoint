from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.My_endpoints.as_view(), name='api_endpoint')
]
