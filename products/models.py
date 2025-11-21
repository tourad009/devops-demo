from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['-created_at']

    def __str__(self):
        return self.name