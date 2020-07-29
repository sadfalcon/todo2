from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Article, status_choices
from webapp.forms import ArticleForm
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
        return render(request, 'article_create.html', context={'form': ArticleForm})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            # article = Article.objects.create(**form.cleaned_data)
            article = Article.objects.create(
                description=form.cleaned_data['description'],
                full_description=form.cleaned_data['full_description'],
                status=form.cleaned_data['status'],
                date_end=form.cleaned_data['date_end']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_update.html', context={'article': article,'status_choices': status_choices,})
    elif request.method == 'POST':
        errors = {}
        article.description = request.POST.get('description')
        if not article.description:
            errors['description'] = 'This field is required'
        article.full_description = request.POST.get('full_description')
        if not article.full_description:
            errors['full_description'] = 'This field is required'
        article.date_end = request.POST.get('date_end')
        if not article.date_end:
            errors['date_end'] = 'This field is required'
        article.status = request.POST.get('status')

        if errors:
            return render(request, 'article_update.html', context={
                'article': article,
                'errors': errors
            })
        article.save()
        return redirect('article_view', pk=article.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
