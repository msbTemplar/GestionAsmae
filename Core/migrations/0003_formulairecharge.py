# Generated by Django 5.1.6 on 2025-05-24 11:06

import Core.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaireCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payement', models.DateTimeField(verbose_name='Date Payement')),
                ('num_facture', models.CharField(max_length=500, verbose_name='Nº Facture')),
                ('date_facture', models.DateField(verbose_name='Date Facture')),
                ('mois', models.CharField(choices=[('01', 'Janvier'), ('02', 'Février'), ('03', 'Mars'), ('04', 'Avril'), ('05', 'Mai'), ('06', 'Juin'), ('07', 'Juillet'), ('08', 'Août'), ('09', 'Septembre'), ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Décembre')], max_length=2, verbose_name='Mois')),
                ('montant_charge', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant Charge')),
                ('image_charge', models.FileField(blank=True, null=True, upload_to='uploads/', validators=[Core.models.validate_file_extension], verbose_name='Fichier de charge')),
                ('charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.charge')),
            ],
        ),
    ]
