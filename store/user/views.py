from django.contrib.auth import login, logout
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm
from .forms import UserCreationForm


class Register(View):

    template_name = 'user/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def logining(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                redirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def password_reset(request):
    return render(request, 'user/password_reset.html')
