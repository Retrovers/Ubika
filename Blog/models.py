from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.template.defaultfilters import slugify

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    auteur = models.ForeignKey(User)
    slug = models.SlugField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Article ,self).save(*args, **kwargs)

class Commentaire(models.Model):
    article = models.ForeignKey(Article)
    contenu = models.TextField()
    auteur = models.ForeignKey(User)
    published_date = models.DateTimeField(auto_now_add=True)
