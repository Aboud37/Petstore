from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django_filters.views import FilterView
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = SellAPet
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['SellAPet'] = SellAPet.objects.all().order_by('-created_at')[:3]
        context['DonateAPet'] = DonateAPet.objects.all().order_by('-created_at')[:3]
        context['SitAPet'] = SitAPet.objects.all().order_by('-created_at')[:3]
        context['SellFood'] = SellFood.objects.all().order_by('-created_at')[:4]
        return context



@login_required(login_url='/se_connecter/')
def sellapet(request):
    form = SellingAPetForm()
    if request.method == 'POST':
        form = SellingAPetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSellaPet.html', context)

@login_required(login_url='/se_connecter/')
def sellapetedit(request, pk):
    selloffer = SellAPet.objects.get(id=pk)
    form = SellingAPetForm(instance=selloffer)

    if request.method == 'POST':
        form = SellingAPetForm(request.POST, request.FILES,instance=selloffer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSellaPetEdit.html', context)

@login_required(login_url='/se_connecter/')
def sitapet(request):
    form = SetingAPetForm()
    if request.method == 'POST':
        form = SetingAPetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSitaPet.html', context)

@login_required(login_url='/se_connecter/')
def sitapetedit(request, pk):
    sitoffer = SitAPet.objects.get(id=pk)
    form = SetingAPetForm(instance= sitoffer)
    if request.method == 'POST':
        form = SetingAPetForm(request.POST, request.FILES, instance= sitoffer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSitaPetEdit.html', context)

@login_required(login_url='/se_connecter/')
def selfood(request):
    form = SellingFoodForm()
    if request.method == 'POST':
        form = SellingFoodForm(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSellFood.html', context)

@login_required(login_url='/se_connecter/')
def selfoodedit(request, pk):
    selfoodoffer = SellFood.objects.get(id= pk)
    form = SellingFoodForm(instance= selfoodoffer)
    if request.method == 'POST':
        form = SellingFoodForm(request.post, request.FILES, instance= selfoodoffer)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormSellFood.html', context)

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class Sit_a_pet_list(FilteredListView):
    model = SitAPet
    template_name = 'shop/SitaPetList.html'
    filterset_class = SittingAPetFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']: SittingAPetFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Sit_a_pet_detail(DetailView):
    model = SitAPet
    template_name = 'shop/SitaPetDetail.html'
    context_object_name = 'garder_un_animal_detail'


class Sell_a_pet_list(FilteredListView):
    model = SellAPet
    template_name = 'shop/SellaPetList.html'
    filterset_class = SellingAPetFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']: SellingAPetFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Sel_a_pet_detail(DetailView):
    model = SellAPet
    template_name = 'shop/SellaPetDetail.html'
    context_object_name = 'vendre_un_animal_detail'


class Sellfoodlist(FilteredListView):
    model = SellFood
    template_name = 'shop/SellFoodList.html'
    context_object_name = 'vendre_alimentation_list'
    filterset_class = SellingFoodFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']: SellingFoodFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Sellfooddetail(DetailView):
    model = SellFood
    template_name = 'shop/SellFoodDetail.html'
    context_object_name = 'vendre_alimentation_detail'


class Donate_a_pet_list(FilteredListView):
    model = DonateAPet
    template_name = 'shop/DonateaPetList.html'
    filterset_class = DonatingAPetFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']: SellingAPetFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Donate_a_pet_detail(DetailView):
    model = DonateAPet
    template_name = 'shop/DonateaPetDetail.html'
    context_object_name = 'offrir_un_animal_detail'

@login_required(login_url='/se_connecter/')
def donateapet(request):
    form = DonationAPetForm()
    if request.method == 'POST':
        form = SellingAPetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormDonateaPet.html', context)

@login_required(login_url='/se_connecter/')
def donateapetedit(request, pk):
    donateoffer = DonateAPet.objects.get(id=pk)
    form = DonationAPetForm(instance=donateoffer)

    if request.method == 'POST':
        form = SellingAPetForm(request.POST, request.FILES,instance=donateoffer)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            return redirect('offres')
    context = {'form': form}
    return render(request, 'shop/FormDonateaPetEdit.html', context)

def contact(request):

    if request.method== 'POST':
        form_name = request.POST['form-name']
        form_email = request.POST['form-email']
        form_subject = request.POST['form-subject']
        form_message = request.POST['form-message']

        send_mail(
            form_name,
            form_email,
            form_message,
            ['abdou371992@gmail.com'],
        )

    return render(request, 'shop/contact.html')



