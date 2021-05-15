from django.contrib import admin
from myapp import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('programming_tools', 'title', 'english_title', 'classify', 'create_time')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'article', 'create_time')


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)

