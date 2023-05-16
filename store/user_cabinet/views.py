from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'user_cabinet/register.html', {'form': form})


def login(request):
    return render(request, 'user_cabinet/login.html')
