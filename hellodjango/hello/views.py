#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json

from datetime import datetime
def home(request):
    # View code here...
    return render(request, 'index.html', {})
def get_html(snippet):
     message = "snippet " + snippet + ".html not found"
     with open(settings.BASE_DIR + "/templates/snippets/" + snippet + ".html") as myfile:
         message = myfile.read()
     return message

def ajax(request):
    try:
        now = datetime.now()
        name = request.GET['name']
        message = "no matching name found to " + name
        if name=="menu_about_me":
            message = get_html("about_me")
        elif name=="menu_welcome":
            message = get_html("welcome")
        elif name=="menu_career":
            message = get_html("career")
        elif name=="menu_schools":
            message = get_html("schools")
        elif name=="menu_hobbies":
            message = get_html("hobbies")
        return HttpResponse(json.dumps({'message': message}))
 
    except Exception as exc:
        print(exc)

def echo(name):
    return ' Hello ' +name + "! The time is " + str(datetime.now())
