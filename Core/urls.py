

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    
    path('enregistrer_charge/', views.enregistrer_charge_view, name='enregistrer_charge'),
    path('liste_des_charges', views.liste_des_charges, name='liste_des_charges'),
    path('actualiser_la_charge/<id_charge>', views.actualiser_la_charge, name='actualiser_la_charge'),
    path('eliminer_la_charge/<id_charge>', views.eliminer_la_charge, name='eliminer_la_charge'),
    
    path('liste_des_formulaire_charges', views.liste_des_formulaire_charges, name='liste_des_formulaire_charges'),
    path('enregistrer_formulaire_charge/', views.enregistrer_formulaire_charge_view, name='enregistrer_formulaire_charge'),
    path('actualiser_formulaire_charge/<id_formulaire_charge>', views.actualiser_formulaire_charge, name='actualiser_formulaire_charge'),
    path('eliminer_formulaire_charge/<id_formulaire_charge>', views.eliminer_formulaire_charge, name='eliminer_formulaire_charge'),
    path('charges/filtre-date/', views.liste_des_formulaire_charges_avec_filtre_Date_facture, name='liste_des_formulaire_charges_avec_filtre_Date_facture'),
    
    path('liste_des_chiffres_affaires', views.liste_des_chiffres_affaires, name='liste_des_chiffres_affaires'),
    path('actualizer_le_chiffre_affaire/<id_chiffre_affaire>', views.actualizer_le_chiffre_affaire, name='actualizer_le_chiffre_affaire'),
    path('eliminer_le_chiffre_affaire/<id_chiffre_affaire>', views.eliminer_le_chiffre_affaire, name='eliminer_le_chiffre_affaire'),
    path('enregistrer_le_chiffre_affaire/', views.enregistrer_le_chiffre_affaire_view, name='enregistrer_le_chiffre_affaire'),

]
