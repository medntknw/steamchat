from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def home(request):
    return HttpResponse('This is the homepage')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })