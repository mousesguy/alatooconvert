from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
# Create your views here.   

def index(request):
    documents = Document.objects.all()
    return render(request, 'main/index.html',{'title': 'das', 'document': documents})

def about(request):
    return render(request, 'main/about.html')

def master(request):
    error = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Something is wrong'
    form = DocumentForm()
    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/master.html', context)