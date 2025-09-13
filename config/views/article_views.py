from django.shortcuts import render
from django.views.generic import ListView
from manual_dic.models import Article

class IndexListView(ListView):
    model = Article
    template_name = 'pages/index.html'