from django.shortcuts import render


def index(request):
    return render(request, 'main/home_page.html')


def about_us(request):
    return render(request, 'main/page_about_us.html')


def contacts(request):
    return render(request, 'main/contacts.html')