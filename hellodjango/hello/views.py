from django.shortcuts import render

def home(request):
    # View code here...
    return render(request, 'index.html', {})
