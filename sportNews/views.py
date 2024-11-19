from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Article
# Create your views here


def home(request):
    categories = Category.objects.filter(is_homepage=True).order_by('ordering')
    articles = Article.objects.filter(category__in=categories,
                                      status='published').order_by('-publish_date')
    context = {
        'categories': categories,
        'articles': articles
    }
    return render(request, 'pages/home.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.filter(is_homepage=True).order_by('ordering')
    articles = Article.objects.filter(category=category , status='published').order_by('-publish_date')
    context = {
        'category': category,  # Category hiện tại
        'categories': categories,  # Danh sách tất cả các categories
        'articles': articles,  # Bài viết của category hiện tại
    }
    
    return render(request, 'pages/category_detail.html', context)

def article_detail(request, id):
    categories = Category.objects.filter(is_homepage=True)
    article = get_object_or_404(Article, id=id)
    context = {
        'categories': categories,
        'article': article
    }
    return render(request, 'pages/article_detail.html', context)

