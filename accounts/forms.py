from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from accounts.models import *


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, error_messages={'unique': 'cette adresse existe'},
                             widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta():
        model = Account
        fields = ("email", "first_name", "last_name", "gouvernerat", 'password1', 'password2')
        widgets = {'gouvernerat': forms.Select(attrs={'class': "form-control"}),
                   'first_name': forms.TextInput(attrs={'class': "form-control"}),
                   'last_name': forms.TextInput(attrs={'class': "form-control"}), }


class AccountAuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Password", max_length=60,
                               widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def cleaned(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('invalid login')


class AccountForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, error_messages={'unique': 'cette adresse existe'},
                             widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta():
        model = Account
        fields = ("email", "first_name", "last_name", "gouvernerat")
        widgets = {'gouvernerat': forms.Select(attrs={'class': "form-control"}),
                   'first_name': forms.TextInput(attrs={'class': "form-control"}),
                   'last_name': forms.TextInput(attrs={'class': "form-control"}), }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "gouvernerat")
        widgets = {'gouvernerat': forms.Select(attrs={'class': "form-control"}),
                   'first_name': forms.TextInput(attrs={'class': "form-control"}),
                   'last_name': forms.TextInput(attrs={'class': "form-control"}), }


class ChangePasswordForm(SetPasswordForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = Account
        fields = ["old_password","new_password1","new_password2" ]


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))

    class Meta:
        model = Account
        fields = ["email"]



