from django.contrib import admin
from Blog.models import Commentaire
from Blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Article, ArticleAdmin)