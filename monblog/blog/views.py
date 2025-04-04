from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

# Liste des articles
class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"  # Nom de la variable dans le template
    ordering = ['-date_publication']  # Articles les plus récents en premier

    def get_queryset(self):
        """Récupère les articles avec leurs images"""
        return Article.objects.all().order_by('-date_publication')

# Détails d'un article
class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"

    def get_context_data(self, **kwargs):
        """Ajoute les articles récents dans le contexte"""
        context = super().get_context_data(**kwargs)
        context['recent_articles'] = Article.objects.exclude(pk=self.object.pk).order_by('-date_publication')[:5]
        return context

# Création d'un nouvel article
class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = "blog/article_form.html"
    success_url = reverse_lazy('article_list')

# Modification d'un article
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = "blog/article_form.html"
    success_url = reverse_lazy('article_list')

# Suppression d'un article
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy('article_list')
