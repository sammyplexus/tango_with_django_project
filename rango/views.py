from django.shortcuts import render

def index(request):
    contextDictionary = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context = contextDictionary)

def about(request):
    return render(request, 'rango/about.html')

# Create your views here.
