from django.shortcuts import render
from webapp.models import Article
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
        article = Article.objects.create(description=description, status=status, date_end=date_end)
        context = {
            'article': article
        }
        return render(request, 'article_view.html', context)


def article_view(request):
    article_id = request.GET.get('pk')
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'article_view.html', context)