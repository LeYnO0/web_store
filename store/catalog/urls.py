from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.show_catalog),
    path('catalog_editor/', views.catalog_editor, name='catalog_editor')
]
