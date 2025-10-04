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

class ArticleListView(ListView): #LoginRequiredMixin,ListView
    model = Article
    template_name = "snippets/article_list.html"
    #def get_queryset(self):
     #   query = self.request.Get.get('query')
        
      #  if query:
       #     article_list = Article.objects.filter(name_icontains=query)
        #else:
         #   article_list = Article.objects.all()
        #return article_list

#class ArticleListView(ListView): #投稿一覧 LoginRequiredMixin,ListView
    #template_name = "snippets/article_list.html"
    

#def article_list(request):
 #   context = {'title': 'Article_list1ページ'}
  #  return render(request,'stella/views/article_list.html', context) 

class ArticleCreateView(CreateView):  #新規作成 LoginRequiredMixin,CreateView
    model = Article
    #queryset = Article.objects.all() #データを全部持ってきて
    field = '__all__'
    #template_name = 'snippets/article_form.html'

class ArticleUpdateView(UpdateView): #LoginRequiredMixin,UpdateView
    model = Article
    fields = '__all__'
    template_name_suffix = '_'

class ArticleDeleteView(DeleteView): #投稿の削除 LoginRequiredMixin,DeleteView
    model = Article
    success_url = reverse_lazy('list')

class ArticleDetailView(DetailView): #投稿の詳細 LoginRequiredMixin,DetailView
    model = Article
    template_name = "snippets/article_detail.html"

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LogoutView): #LoginRequiredMixin, LogoutView
    template_name = 'top.html'


class BookmarkListView(UpdateView):
    template_name = "snippets/bookmark_list.html"

'''
class Bookmark(request, pk): #お気に入り登録LoginRequiredMixin, 
    model = Article
    template_name = "snippets/bookmark_list.html"
    article = get_object_or_404(Article, pk=pk)
    request.user.bookmark.add(Article)
    
  return redirect()
'''



