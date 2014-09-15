from django.shortcuts import render
from django.http import HttpResponse
import json

from datetime import datetime
def home(request):
    # View code here...
    return render(request, 'index.html', {})

def ajax(request):
    try:
        name = request.GET['name']
        message = echo(name) 
        return HttpResponse(json.dumps({'message': message})) 
    except Exception as exc:
        print(exc)

def echo(name):
    return ' Hello ' +name + "! The time is " + str(datetime.now())
