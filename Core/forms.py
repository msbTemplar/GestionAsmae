from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Charge, FormulaireCharge, ChiffreAffaire
from django.core.validators import MinValueValidator, MaxValueValidator

class EnregistrerChiffreAffaireForm(forms.ModelForm):
    class Meta:
        model = ChiffreAffaire
        fields = '__all__'
        widgets = {
            'annee': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez l\'année',
                'name': 'annee',
            }),
            'montant': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le montant en dirhams (MAD)',
                'step': '0.01',
                'name': 'montant',
            }),
        }
        labels = {
            'annee': "Année",
            'montant': "Montant (MAD)",
        }

class EnregistrerFormulaireChargeForm(forms.ModelForm):
    class Meta:
        model = FormulaireCharge
        fields = '__all__'
        widgets = {
            'date_payement': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date de paiement',
                'type': 'date'
            }),
            'charge': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Charge'
            }),
            'num_facture': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nº Facture'
            }),
            'date_facture': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date Facture',
                'type': 'date'
            }),
            'mois': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Mois'
            }),
            'montant_charge': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Montant Charge',
                'min': '0',
                'step': '0.01'
            }),
            'image_charge': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'formFile'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Cargar dinámicamente las opciones de Charge si es necesario
        self.fields['charge'].queryset = Charge.objects.all()

class EnregistrerChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
        widgets = {'nome_charge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire la charge','name':'nome_charge'}),}
