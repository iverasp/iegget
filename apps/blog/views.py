from django.shortcuts import render
from wiki.models import Article
from wiki.core.markdown import article_markdown
from django.utils.safestring import mark_safe

PREVIEW_ARTICLE_LENGTH = 300

def index(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    articles = []
    for article in recent_articles:
        articles.append(render_article(article))
        print(article.current_revision.title)
        print(article.current_revision.content[0:40])
        print(article.get_absolute_url())
        print(render_article(article))
    print(articles)
    context = {
        'articles': articles,
    }
    return render(request, 'blog.html', context)

def about(request):
    return render(request, 'about.html')

def render_article(article):
    if len(article.current_revision.content) > PREVIEW_ARTICLE_LENGTH:
        return {
            'render' :mark_safe(article_markdown(
            article.current_revision.content[0:PREVIEW_ARTICLE_LENGTH] + ' (...)',
            article.current_revision
            )),
            'url': article.get_absolute_url(),
            'title': article.current_revision.title
        }
    return {
        'render' :mark_safe(article_markdown(
        article.current_revision.content,
        article.current_revision
        )),
        'url': article.get_absolute_url(),
        'title': article.current_revision.title
    }
