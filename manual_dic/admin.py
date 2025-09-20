# 管理画面設定

from manual_dic.forms import UserCreationForm
from django.contrib import admin
from manual_dic.models import Article, Category, Tag, CustomUser, Profile  #User→CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
 
 
class TagInline(admin.TabularInline):
    model = Article.tags.through
 
 
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
    list_display = ['username', 'user_id', 'email']
    list_filter = ()
    ordering = ()　#項目の表示並び替え設定
    filter_horizontal = ()
 
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
 
    add_form = UserCreationForm
 
    inlines = (ProfileInline,)
 
 
admin.site.register(Article, ArticleAdmin)   #項目新規追記(register)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(CustomUser, CustomUserAdmin) #User→CustomUser
admin.site.unregister(Group)  #今ある表示を非表示（unregister）に