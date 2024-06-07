from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('user.html/', views.show_user, name='show_user'),

]