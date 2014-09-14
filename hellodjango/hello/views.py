from django.shortcuts import render
from django.http import HttpResponse
import json

from datetime import datetime
def home(request):
    # View code here...
    return render(request, 'index.html', {})

def ajax(request):
    print "in ajax"
    try:
        message = ' Hello Ajax ' + str(datetime.now()) 
        return HttpResponse(json.dumps({'message': message})) 
    except Exception as exc:
        print(exc)
