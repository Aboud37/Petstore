from django import forms

from .models import *
import django_filters


class SellingAPetFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    race = django_filters.ModelChoiceFilter(queryset= Race.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    sexe = django_filters.AllValuesFilter(choices=SellAPet.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = SellAPet
        fields = ['race', 'category','sexe']

class DonatingAPetFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    race = django_filters.ModelChoiceFilter(queryset= Race.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    sexe = django_filters.AllValuesFilter(choices=DonateAPet.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = DonateAPet
        fields = ['race', 'category','sexe']


class SittingAPetFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-control'}))
    race = django_filters.ModelChoiceFilter(queryset=Race.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-control'}))
    sexe = django_filters.AllValuesFilter(choices=SellAPet.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = SitAPet
        fields = ['race', 'category','sexe',]



class SellingFoodFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = SellFood
        fields = ['category']



