from django import forms
from django.contrib.auth.forms import SetPasswordForm

from .models import *


class SellingAPetForm(forms.ModelForm):
    class Meta:
        model= SellAPet
        fields= ('category', 'race', 'description', 'price', 'quantity','thumbnail', 'image1','image2','image3', 'sexe')

        widgets ={'category': forms.Select(attrs={'class':"form-control" }),
                  'race': forms.Select(attrs={'class': "form-control"}),
                  'description': forms.Textarea(attrs={'class': "form-control"}),
                  'price': forms.TextInput(attrs={'class': "form-control"}),
                'quantity': forms.TextInput(attrs={'class': "form-control"}),
                 'sexe': forms.Select(attrs={'class': "form-control"}),
                  'thumbnail': forms.FileInput(attrs={'class': "form-control"}),
                  'image1': forms.FileInput(attrs={'class': "form-control"}),
                  'image2': forms.FileInput(attrs={'class': "form-control"}),
                  'image3': forms.FileInput(attrs={'class': "form-control"}),
              }


class SetingAPetForm(forms.ModelForm):
    class Meta:
        model= SitAPet
        fields= ('category', 'race', 'description', 'price', 'pets','thumbnail', 'image1','image2','image3', 'sexe','garden', 'house', 'available_from', 'available_to')

        widgets ={'category': forms.Select(attrs={'class':"form-control" }),
                  'race': forms.Select(attrs={'class': "form-control"}),
                  'description': forms.Textarea(attrs={'class': "form-control"}),
                  'price': forms.TextInput(attrs={'class': "form-control"}),
                'pets': forms.CheckboxInput(attrs={'class': "form-check-input"}),
                 'sexe': forms.Select(attrs={'class': "form-control"}),
                  'garden': forms.CheckboxInput(attrs={'class': "form-check-input"}),
                  'house': forms.CheckboxInput(attrs={'class': "form-check-input"}),
                  'available_from' : forms.DateInput(attrs={'class': "form-control"}),
                  'available_to' : forms.DateInput(attrs={'class': "form-control"}),
                  'thumbnail': forms.FileInput(attrs={'class': "form-control"}),
                  'image1': forms.FileInput(attrs={'class': "form-control"}),
                  'image2': forms.FileInput(attrs={'class': "form-control"}),
                  'image3': forms.FileInput(attrs={'class': "form-control"}),
              }

class SellingFoodForm(forms.ModelForm):
    class Meta:
        model= SellFood
        fields= ('brand','category', 'description', 'price','quantity','thumbnail', 'image1','image2','image3',)

        widgets ={'brand': forms.TextInput(attrs={'class': "form-control"}),
                  'category': forms.Select(attrs={'class':"form-control" }),
                  'description': forms.Textarea(attrs={'class': "form-control"}),
                  'price': forms.TextInput(attrs={'class': "form-control"}),
                  'quantity': forms.TextInput(attrs={'class': "form-control"}),
                  'thumbnail': forms.FileInput(attrs={'class': "form-control"}),
                  'image1': forms.FileInput(attrs={'class': "form-control"}),
                  'image2': forms.FileInput(attrs={'class': "form-control"}),
                  'image3': forms.FileInput(attrs={'class': "form-control"}),
              }


class DonationAPetForm(forms.ModelForm):
    class Meta:
        model= SellAPet
        fields= ('category', 'race', 'description', 'quantity','thumbnail', 'image1','image2','image3', 'sexe')

        widgets ={'category': forms.Select(attrs={'class':"form-control" }),
                  'race': forms.Select(attrs={'class': "form-control"}),
                  'description': forms.Textarea(attrs={'class': "form-control"}),
                'quantity': forms.TextInput(attrs={'class': "form-control"}),
                 'sexe': forms.Select(attrs={'class': "form-control"}),
                  'thumbnail': forms.FileInput(attrs={'class': "form-control"}),
                  'image1': forms.FileInput(attrs={'class': "form-control"}),
                  'image2': forms.FileInput(attrs={'class': "form-control"}),
                  'image3': forms.FileInput(attrs={'class': "form-control"}),
              }