from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'user_cabinet/authorization.html', {'form': form})
