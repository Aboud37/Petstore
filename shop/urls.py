from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', Home.as_view() , name='home'),
    #Forms
    path('vendre_un_animal/', views.sellapet, name='vendre'),
    path('vendre_un_animal_modifier/<str:pk>', views.sellapetedit, name='vendre_edit'),
    path('offrir_un_animal/', views.donateapet, name='offrir'),
    path('offrir_un_animal_modifier/<str:pk>', views.donateapetedit, name='offrir_edit'),
    path('garder_un_animal/', views.sitapet, name='garder'),
    path('garder_un_animal_modifier/<str:pk>', views.sitapetedit, name='garder_edit'),
    path('vendre_alimentation/', views.selfood, name='vendre_alimentation'),
    path('vendre_alimentation_modifier/<str:pk>', views.selfoodedit, name='vendre_alimentation_edit'),
    #Shop
    path('garder_un_animal_list/', Sit_a_pet_list.as_view(), name='garder_un_animal'),
    path('acheter_un_animal_list/', Sell_a_pet_list.as_view(), name='acheter_un_animal'),
    path('offrir_un_animal_list/', Donate_a_pet_list.as_view(), name='offrir_un_animal'),
    path('acheter_nouriture_animal/', Sellfoodlist.as_view(), name='acheter_nouriture_animal'),
    path('vendre_un_animal_list/<int:pk>', Sel_a_pet_detail.as_view(), name='vendre_un_animal_detail'),
    path('offrir_un_animal_list/<int:pk>', Donate_a_pet_detail.as_view(), name='offrir_un_animal_detail'),
    path('garder_un_animal_list/<int:pk>', Sit_a_pet_detail.as_view(), name='garder_un_animal_detail'),
    path('vendre_nouriture_animal/<int:pk>', Sellfooddetail.as_view(), name='vendre_nouriture_detail'),
    # Others
    path('contact/', views.contact, name='contact'),
]
