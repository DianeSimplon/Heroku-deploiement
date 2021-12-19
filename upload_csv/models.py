from django.db import models

# Create your models here.
class Upload_csv(models.Model):
    #definir les champs
    id_lot = models.CharField(max_length=200, null=True)
    nb_piece = models.FloatField(null=True)
    typologie = models.CharField(max_length=200, null=True)
    prix_tva_reduite = models.FloatField(null=True)
    prix_tva_normale = models.FloatField(null=True)
    prix_HT = models.FloatField(null=True)
    prix_m2_HT = models.FloatField(null=True)
    prix_m2_TTC = models.FloatField(null=True)
    surface = models.FloatField(null=True)
    etage = models.FloatField(null=True)
    orientation = models.CharField(max_length=200, null=True)
    exterieur = models.BooleanField(null=True)
    balcony =  models.BooleanField(null=True)
    garden =  models.BooleanField(null=True)
    parking = models.FloatField(null=True)
    nom_programme = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    departement = models.FloatField(null=True)
    date_fin_programme = models.CharField(max_length=200, null=True)
    adresse_entiere = models.CharField(max_length=200, null=True)
    promoteur = models.CharField(max_length=200, null=True)
    date_extraction = models.DateField(auto_now_add=True, null=True)
    