from django.urls import path
from rules import views

app_name = 'rules'
urlpatterns = [
    path('user/', views.UserDetail.as_view(), name='user-detail'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
]