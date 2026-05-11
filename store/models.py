from django.db import models

# Create your models here.
"""
Produit
-Nom
-Prix
-La quantite en stock
-Une description
-Une image

"""
class Produit(models.Model) :
    nom = models.CharField(max_length=128)
    prix = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="Articles" , blank=True , null=True)

