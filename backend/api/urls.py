from django.urls import path
from .views import UserId, UserName, UserList

urlpatterns = [
    path('user/<int:pk>/', UserId.as_view()),
    path('list/userList/', UserList.as_view()),
    path('name/<int:pk>/', UserName.as_view()),
]
