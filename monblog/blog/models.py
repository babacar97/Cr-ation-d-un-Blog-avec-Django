from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)  # Titre de l'article
    contenu = models.TextField()  # Contenu de l'article
    date_publication = models.DateTimeField(auto_now_add=True)  # Date automatique
    auteur = models.CharField(max_length=100)  # Auteur de l'article
    image = models.ImageField(upload_to='articles/', blank=True, null=True)  # Image facultative

    def __str__(self):
        return self.titre  # Affiche le titre dans l'admin Django


