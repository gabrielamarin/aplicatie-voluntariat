from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

def chat_index(request):
    return render(request, 'communication/chat_index.html')


def room(request, room_name):
    return render(request, 'communication/room.html', {
        'room_name': room_name
    })