from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')  # Colonnes affichées dans l'admin
    search_fields = ('titre', 'auteur')  # Barre de recherche par titre/auteur
