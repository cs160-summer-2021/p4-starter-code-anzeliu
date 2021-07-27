from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),

    path('home_variant', views.home_variant, name='home_variant'),
    
    path('main_hall', views.main_hall, name='main_hall'),

    path('main_hall_variant', views.main_hall_variant, name='main_hall_variant'),

    path('themed_room_v1', views.themed_room_v1, name='themed_room_v1'),

    path('themed_room_v1_variant', views.themed_room_v1_variant, name='themed_room_v1_variant'), 

    path('themed_room_v2', views.themed_room_v2, name='themed_room_v2'),
    
    path('themed_room_v2_variant', views.themed_room_v2_variant, name='themed_room_v2_variant'),
    
    path('upload_artwork', views.upload_artwork, name='upload_artwork'),
    
    path('drawing_pad', views.drawing_pad, name='drawing_pad'),

    path('drawing_pad_variant', views.drawing_pad_variant, name='drawing_pad_variant'),
    
    path('color_picker', views.color_picker, name='color_picker'),

    path('color_picker_variant', views.color_picker_variant, name='color_picker_variant'),
    
    path('chat_room', views.chat_room, name='chat_room'),
    
    path('museum_display', views.museum_display, name='museum_display'),
    
    path('save_artwork', views.save_artwork, name='save_artwork'),
    
    path('save_artwork_new', views.save_artwork_new, name='save_artwork_new'),
    
    path('save_artwork_variant', views.save_artwork_variant, name='save_artwork_variant'),
    
    path('<str:room_name>/', views.room, name='room')
]
