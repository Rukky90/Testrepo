from django.urls import path, include
from .import views
app_name = 'band'
urlpatterns =[
    path('home/', views.home, name ='home'),
    path('about/',views.about, name ='about'),
    path('discography/',views.discography, name= 'discography'),
]
