from django.urls import path, include

from . import views
from .views import Register
import django.contrib.auth.urls

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view()),
    path('login/', views.logining, name='logining'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('logout/', views.logout_view, name='logout')
]
