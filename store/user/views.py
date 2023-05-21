from django.contrib.auth import login, logout
from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import UserLoginForm, UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'user/password_reset_form.html'
    email_template_name = 'user/password_reset_email.html'
    subject_template_name = 'user/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


def logining(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def password_reset(request):
    # if request.method == 'POST':
    return render(request, 'user/password_reset_form.html')
