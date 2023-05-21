from django.shortcuts import render
from .models import CatalogElements

def show_catalog(request):
    elements = CatalogElements.objects.all()
    return render(request, 'catalog/catalog.html', {'elements': elements})


def catalog_editor(request):
    return render(request, 'catalog/catalog_editor_page.html')
