from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from shop.models import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def loginpage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    form = AccountAuthenticationForm()
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('profile')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)
    return redirect('home')


def registerpage(request):
    form = AccountCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            row_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=row_password)
            form.save()
            return redirect('se_connecter')
        else:
            return render(request, 'accounts/register.html', context)

    return render(request, 'accounts/register.html', context)

@login_required(login_url='/se_connecter/')
def MyProfile(request):
    user_form = AccountForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="accounts/profile.html",
                  context={"user": request.user, "user_form": user_form, "profile_form": profile_form,})

@login_required(login_url='/se_connecter/')
def MyProfileedit(request):
    user_form = AccountForm(instance=request.user)

    if request.method == "POST":
        user_form = AccountForm(request.POST,instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')

    return render(request=request, template_name="accounts/profile_edit.html",
                  context={"user": request.user, "user_form":user_form,})

@login_required(login_url='/se_connecter/')
def change_password(request):
    form = ChangePasswordForm(request.user)
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Votre mot de pase est changé avec succées")
            return redirect('profile')
        else:
            messages.error(request, "Votre mot de pase est changé avec succées")
    context = {"form":form}
    return render(request, 'accounts/changer_mdp.html',context)


class Offers(LoginRequiredMixin, ListView):
    model = SellAPet
    template_name = 'accounts/Myoffer.html'
    login_url = '/se_connecter/'

    def get_context_data(self, **kwargs):
        context = super(Offers, self).get_context_data(**kwargs)
        context['SellAPet'] = SellAPet.objects.filter(user=self.request.user)
        context['SitAPet'] = SitAPet.objects.filter(user=self.request.user)
        context['SellFood'] = SellFood.objects.filter(user=self.request.user)
        return context
