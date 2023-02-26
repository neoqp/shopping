from django.shortcuts import *
from .models import note

# Create your views here.

def create(request):
    if request.method=='POST':
        article = note()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('note:detail')
    
    else:
        return render(request, 'create.html')

def detail(request):
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