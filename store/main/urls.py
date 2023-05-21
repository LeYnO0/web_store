from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_us),
    path('contacts/', views.contacts),
]