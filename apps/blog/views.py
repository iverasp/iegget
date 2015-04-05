from django.shortcuts import render
from wiki.models import Article
from wiki.core.markdown import article_markdown
from django.utils.safestring import mark_safe
from models import Welcome, About

PREVIEW_ARTICLE_LENGTH = 300

def index(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    articles = []
    for article in recent_articles:
        articles.append(render_article(article))
    welcome = Welcome.objects.get(enabled=True)
    context = {
        'articles': articles,
        'welcome': welcome,
    }
    return render(request, 'blog.html', context)

def about(request):
    about = About.objects.get(enabled=True)
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

def render_article(article):
    if len(article.current_revision.content) > PREVIEW_ARTICLE_LENGTH:
        render = mark_safe(article_markdown(
            article.current_revision.content[0:PREVIEW_ARTICLE_LENGTH] + mark_safe('...'),
            article
        ))  + mark_safe('<p><a href="') \
            + mark_safe(article.get_absolute_url()) \
            + mark_safe('">(more...)</a></p>')
    else:
        render = mark_safe(article_markdown(
            article.current_revision.content,
            article
        ))
    return {
        'render': render,
        'url': article.get_absolute_url(),
        'title': article.current_revision.title
    }
