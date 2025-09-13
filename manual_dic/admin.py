# 管理画面設定

from django.contrib import admin
from manual_dic.models import Article, Category, Tag  #baseが行方不明
from django.contrib.auth.models import Group
 
 
class TagInline(admin.TabularInline):
    model = Article.tags.through
 
 
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']
 
 
admin.site.register(Article, ArticleAdmin)   #項目新規追記(register)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)  #今ある表示を非表示（unregister）に