from django.urls import path, include
from .import views
app_name = 'band'
urlpatterns =[
    path('home/', views.home, name ='home'),
    path('about/',views.about, name ='about'),
    path('discography/',views.discography, name= 'discography'),
]
"""
URL configuration for the band app.

The `urlpatterns` list routes URLs to views. 

Routes:
    - 'home/': Renders the home page.
    - 'about/': Renders the about page.
    - 'discography/': Renders the discography page with a list of albums.

Modules:
    - path: Function to define URL patterns.
    - include: Function to include other URL configurations.
    - views: Module containing view functions for the band app.
"""