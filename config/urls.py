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
from stella import views
from stella.views import ArticleListView #不要？
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls), #管理画面

    path('', views.TopView.as_view(), name="top"), #トップページ

    #path('article_list/', views.article_list, name="article_list"), #投稿一覧 URL部は可views.py調整要 トップから遷移→top.htmlをカレンフォルダ

    path('stella/new/', views.ArticleCreateView.as_view(), name="new"), #新規作成

    path('article_list/', views.ArticleListView.as_view(), name="article_list"),  #投稿一覧 ここにヘッダーのリンク設定？

    path('stella/edit/<int:pk>', views.ArticleUpdateView.as_view(), name="edit"),

    path('stella/delete/<int:pk>', views.ArticleDeleteView.as_view(), name="delete"),

    path('stella/detail/views', views.ArticleDetailView.as_view(), name="detail"), #投稿詳細

    path('login/', views.LoginView.as_view(), name="login"), #topに対して一つ前のフォルダにhtml。どう表記？
    
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('signup/', views.SignUpView.as_view(), name="signup"), #アカウント作成

    path('accountupdate/', views.AccountUpdateView.as_view(), name="accountupdate"), #アカウント

    path('account/', views.Account.as_view(), name="account"),

    path('bookmark_list/', views.BookmarkListView.as_view(), name="bookmark_list"), #お気に入り

    #path('bookmark/<int:pk>/', views.followPlace, name='bookmark'), #お気に入り

    #path('bookmark/remove/<str:pk>/', views.remove_from_bookmark),
    #path('bookmark/add/', views.AddBookmarkView.as_view()),
    #path('bookmark/', views.BookmarkListView.as_view()), 

    
]
