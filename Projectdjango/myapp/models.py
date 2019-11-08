from email.policy import default
from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='image/Categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'



class SousCategorie(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='categorie_sous')
    nom = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image/SousCategorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'SousCategorie'
        verbose_name_plural = 'SousCategories'


class Tag(models.Model):
    nom = models.CharField(max_length=50) 
    status = models.BooleanField(default=True) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'

      
class Produit(models.Model):
    souscategorie = models.ForeignKey(SousCategorie,on_delete=models.CASCADE,related_name='Souscategorie_produit')
    titre = models.CharField(max_length=255)
    descriprion = models.TextField()
    image = models.ImageField(upload_to='image/Produit')
    tag = models.ManyToManyField(Tag)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'