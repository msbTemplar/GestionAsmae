from django.contrib import admin
from .models import PasswordReset, Charge, FormulaireCharge, ChiffreAffaire

admin.site.register(PasswordReset)
admin.site.register(Charge)
admin.site.register(FormulaireCharge)
@admin.register(ChiffreAffaire)
class ChiffreAffaireAdmin(admin.ModelAdmin):
    list_display = ('annee', 'montant')
    ordering = ('-annee',)