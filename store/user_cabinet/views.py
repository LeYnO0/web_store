from django.shortcuts import render


def show_user_cabinet(request):
    return render(request, 'user_cabinet/user_cabinet.html')
