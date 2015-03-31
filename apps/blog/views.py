from django.shortcuts import render
from wiki.models import Article

def index(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    for article in recent_articles:
        print(article.current_revision.title)
        print(article.current_revision.content[0:40])
        print(article.get_absolute_url())
    context = {
        'articles': recent_articles,
    }
    return render(request, 'blog.html', context)

def about(request):
    return render(request, 'about.html')
