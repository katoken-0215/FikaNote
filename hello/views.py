#!/usr/bin/env python
#coding:utf-8
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    episodes = []
    episodes.append({
        'agenda':'あれとこれをそれしました' ,
        'year' : '2015',
        'date' : '05/Jan',
        'title' : 'はじめてのFika',
        'number' : 1
        })
    episodes.append({
        'agenda':'hogeとfugaについて話しました' ,
        'year' : '2015',
        'date' : '09/Jan',
        'title' : '開発者のこれからについて',
        'number' : 2
        })
    return render(request, 'index.html', 
                  {'episodes': episodes
                  } )

def episode(request, number):
    persons = []
    persons.append({'name':'Kosuke Nagano', 'twitter':'gm_kou', 
                    'avatar':'https://pbs.twimg.com/profile_images/780617517/IMG_0151_400x400.JPG'})
    persons.append({'name':'Satoshi Nagano', 'twitter':'sassy_watson',
                    'avatar':'https://pbs.twimg.com/profile_images/1197190603/bird_bigger_400x400.png'})
    shownotes = []
    shownotes.append({'id':1, 'url':'http://www.google.com', 'title':'Google', 'introducer':'gm_kou' })
    shownotes.append({'id':2, 'url':'http://www.yahoo.co.jp', 'title':'Yahoo', 'introducer':'sassy_watson' })
    episode = {
        'agenda':'あれとこれをそれしました' ,
        'year' : '2015',
        'date' : '09/Jan',
        'title' : 'はじめてのFika',
        'number' : 1,
        'person' : ['gm_kou', 'sassy_watson'],
        'shownote' : [1, 2]
        }
    return render(request, 'episode.html', 
                  {'episode': episode, 
                   'shownotes':shownotes, 
                   'persons':persons 
                   } )

def agenda(request):
    agendas = []
    agendas.append({'id':1, 'url':'http://www.google.com', 'title':'Google', 'introducer':'gm_kou' })
    agendas.append({'id':2, 'url':'http://www.yahoo.co.jp', 'title':'Yahoo', 'introducer':'sassy_watson' })
    return render(request, 'agenda.html', 
                  {'agendas': agendas
                  } )

def add(request):
    if request.method == 'POST':
        content = 'not support this method'
        return HttpResponse(content, content_type='text/plain')
    else:
        content = 'not support this method'
        return HttpResponse(content, content_type='text/plain')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

