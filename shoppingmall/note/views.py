from django.shortcuts import *
from .models import note

# Create your views here.

def create(request):
    if request.method=='POST':
        article = note()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('note:detail', article.pk) #redirect로 만들어 진 페이지로 이동하게
    
    else:
        return render(request, 'create.html')

def detail(request, pk):
    # article = Article.objects.get(pk=pk) 

    article = get_object_or_404(note, pk=pk)
    # Article.objects.get을 써도 되지만 get_object_or_404를 쓸 경우 pk값이 없을 경우 404 나오게

    context = {
        'note': article
    }
    return render(request, 'detail.html', context)

def update(request, pk):
    article = get_object_or_404(note, pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('note:detail', article.pk)

def delete(request, pk):
    article = get_object_or_404(note, pk=pk)
    article.delete()
    return redirect('note:index')

def review(request):
    return render(request, 'reviews.html')