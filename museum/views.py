# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'museum/index.html')

def home(request):
    return render(request, 'museum/home.html')

def home_variant(request):
    return render(request, 'museum/home_variant.html')

def chat_room(request):
    return render(request, 'museum/chat_room.html')

def color_picker(request):
    return render(request, 'museum/color_picker.html')

def color_picker_variant(request):
    return render(request, 'museum/color_picker_variant.html')

def drawing_pad(request):
    return render(request, 'museum/drawing_pad.html')

def drawing_pad_variant(request):
    return render(request, 'museum/drawing_pad_variant.html')

def main_hall(request):
    return render(request, 'museum/main_hall.html')

def main_hall_variant(request):
    return render(request, 'museum/main_hall_variant.html')

def museum_display(request):
    return render(request, 'museum/museum_display.html')

def themed_room_v1(request):
    return render(request, 'museum/themed_room_v1.html')

def themed_room_v1_variant(request):
    return render(request, 'museum/themed_room_v1_variant.html')    

def themed_room_v2(request):
    return render(request, 'museum/themed_room_v2.html')

def themed_room_v2_variant(request):
    return render(request, 'museum/themed_room_v2_variant.html')

def upload_artwork(request):
    return render(request, 'museum/upload_artwork.html')

def save_artwork(request):
    return render(request, 'museum/save_artwork.html')

def save_artwork_variant(request):
    return render(request, 'museum/save_artwork_variant.html')    

def save_artwork_new(request):
    return render(request, 'museum/save_artwork_new.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
