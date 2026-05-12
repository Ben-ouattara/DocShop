from django.shortcuts import render
from store.models import Produit

def index(request):
    Produits = Produit.objects.all()
    return render(request, 'store/index.html', context={'Produits':Produits})

