"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) 
"""
from django.contrib import admin
from django.urls import path
from manual_dic import views
from manual_dic.views import IndexListView

urlpatterns = [
    path('admin/', admin.site.urls), #管理画面

    path('', views.TopView.as_view(), name="top"), #トップページ

    path('manual_dic/views', views.ArticleListView.as_view(), name="list") #投稿一覧

    path('manual_dic/new/', views.ArticleCreateView.as_view(), name="new"), #新規作成

    #path('article/',　{% url 'article_list'}, name="list"),  投稿一覧 ここにヘッダーのリンク設定？

    path('manual_dic/edit/<int:pk>', views.ArticleUpdateView.as_view(), name="edit"),

    path('manual_dic/delete/<int:pk>', views.ArticleDeleteView.as_view(), name="delete"),

    path('manual_dic/detail/views', views.ArticleDetailView.as_view(), name="detail"), #投稿詳細

    path('login/', views.LoginView.as_view(), name="login"),
    
    path('logout/', views.LogoutView.as_view(), name="logout"),

    
]
