from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Article
from django.http import HttpResponseNotAllowed
# Create your views here.
def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_end = request.POST.get('date_end')
        if date_end == '':
            article = Article.objects.create(description=description, status=status)
        else:
            article = Article.objects.create(description=description, status=status, date_end=date_end)

        context = {
            'article': article
        }
        url = reverse('article_view', kwargs={'pk': article.pk})
        return HttpResponseRedirect(url)
    else:
        HttpResponseNotAllowed(permitted_methods=['GET','POST'])


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)
