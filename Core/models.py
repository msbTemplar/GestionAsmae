from django.db import models
from django.contrib.auth.models import User
import uuid


class Charge(models.Model):
        nome_charge = models.CharField('Une Charge', max_length=120)
        
        def __str__(self) -> str:
            return self.nome_charge

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Obtener la extensión del archivo
    valid_extensions = ['.pdf', '.xls', '.xlsx', '.doc', '.docx','.jpg','.png', '.jpeg']  # Extensiones permitidas
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Sube archivos PDF, XLS, XLSX, DOC o DOCX.')  

class FormulaireCharge(models.Model):
    MOIS_CHOICES = [
        ('01', 'Janvier'),
        ('02', 'Février'),
        ('03', 'Mars'),
        ('04', 'Avril'),
        ('05', 'Mai'),
        ('06', 'Juin'),
        ('07', 'Juillet'),
        ('08', 'Août'),
        ('09', 'Septembre'),
        ('10', 'Octobre'),
        ('11', 'Novembre'),
        ('12', 'Décembre'),
    ]
    date_payement=models.DateField('Date Payement')
    charge=models.ForeignKey(Charge, blank=True, null=True, on_delete=models.CASCADE)
    num_facture = models.CharField('Nº Facture', max_length=500)
    date_facture_du=models.DateField('Date Facture Du')
    date_facture_au=models.DateField('Date Facture Au', null=True, blank=True)
    mois = models.CharField('Mois', max_length=2, choices=MOIS_CHOICES)
    #au=models.DateField('Au')
    montant_charge = models.DecimalField('Montant Charge', max_digits=10, decimal_places=2)  # Agregar max_digits y decimal_places
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Fichier de charge', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireCharge Charge {self.charge} Date Facture DU {self.date_facture_du} Nº Facture {self.num_facture} avec le montant {self.montant_charge} "

class ChiffreAffaire(models.Model):
    annee = models.PositiveIntegerField("Année")
    montant = models.DecimalField("Montant (MAD)", max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Chiffre d'affaire"
        verbose_name_plural = "Chiffres d'affaires"
        unique_together = ['annee']

    def __str__(self):
        return f"{self.annee} - {self.montant} MAD"

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"