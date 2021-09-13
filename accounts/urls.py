from django.urls import path
from .import views
from .views import *
from django.contrib.auth import views as auth_views
from accounts.forms import *
urlpatterns = [
    #Authentification
    path('se_connecter/', views.loginpage, name='se_connecter'),
    path('se_deconnecter/', views.log_out, name='se_deconnecter'),
    path('s_inscrire/', views.registerpage, name='s_inscrire'),
    #Profile
    path('mon_profile/', views.MyProfile, name='profile'),
    path('mon_profile_edit/', views.MyProfileedit, name='profile_edit'),
    path('mes_offres/', Offers.as_view(), name='offres'),
    #Password
    path('changer_mot_de_passe/', views.change_password, name='changer_mdp'),
    path('recuperer_mot_de_passe_etape_1/', auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html', form_class= ResetPasswordForm), name ='reset_password'),
    path('recuperer_mot_de_passe_envoye/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name ='password_reset_done'),
    path('recuperer_mot_de_passe/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', ), name ='password_reset_confirm'),
    path('recuperer_mot_de_passe_termine/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name ='password_reset_complete'),
]
