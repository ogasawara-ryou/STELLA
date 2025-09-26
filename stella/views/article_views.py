from django.shortcuts import render, redirect, get_object_or_404 #後ろ二つ:お気に入り登録
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from stella.models import Article
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView): #トップページ
    template_name = "snippets/top.html"

class IndexListView(ListView):
    model = Article
    template_name = 'pages/index.html'
    def get_queryset(self):
        query = self.request.Get.get('query')
        
        if query:
            article_list = Article.objects.filter(name_icontains=query)
        else:
            article_list = Article.objects.all()
        return article_list

class ArticleListView(LoginRequiredMixin,ListView): #投稿一覧
    template_name = "snippets/article_list.html"

class ArticleCreateView(LoginRequiredMixin,CreateView):  #新規作成
    model = Article
    field = '__all__'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = '__all__'
    template_name_suffix = '_'

class ArticleDeleteView(LoginRequiredMixin,DeleteView): #投稿の削除
    model = Article
    success_url = reverse_lazy('list')

class ArticleDetailView(LoginRequiredMixin,DetailView): #投稿の詳細
    model = Article
    template_name = "snippets/article_detail.html"

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'

class Bookmark(LoginRequiredMixin, request, pk): #お気に入り登録
    model = Article
    template_name = "snippets/bookmark_list.html"
    article = get_object_or_404(Article, pk=pk)
    request.user.bookmark.add(Article)
    return redirect('stella:index')



