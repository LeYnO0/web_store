from django.urls import path
from . import views
from .views import Register, ResetPasswordView
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', views.logining, name='logining'),
    path('password-reset/', ResetPasswordView.as_view(),  name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
]
