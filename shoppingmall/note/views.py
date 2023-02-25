from django.shortcuts import *
from .models import note

# Create your views here.

def create(request):
    if request.method=='POST':
        article = note()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('note:detail') #redirect로 만들어 진 페이지로 이동하게
    
    else:
        return render(request, 'create.html')

def detail(request):
    # article = Article.objects.get(pk=pk) 
    '''
    last_pk = note.objects.latest('content').pk
    article={}
    for i in range(1,last_pk+1):
        article[chr(i+1)] 
        tmp = get_object_or_404(note, pk=i)
    # Article.objects.get을 써도 되지만 get_object_or_404를 쓸 경우 pk값이 없을 경우 404 나오게
    '''

    article = note.objects.all()
    context = {
        'note': article
    }
    return render(request, 'detail.html', context)

def update(request, pk):
    if request.method=='POST':
        article = get_object_or_404(note, pk=pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('/note', article.pk)
    else:
        return render(request, 'update.html')

def delete(request, pk):
    article = get_object_or_404(note, pk=pk)
    article.delete()
    return redirect('/note')

def review(request):
    return render(request, 'reviews.html')