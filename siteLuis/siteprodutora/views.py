from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def sobre(request):
    return render(request, 'sobre.html')

def shows(request):
    return render(request, 'shows.html')

def contato(request):
    return render(request, 'contato.html')