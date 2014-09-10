from django.shortcuts import render, get_object_or_404
from chat.models import ChatRoom

def index(request):
    chat_rooms = ChatRoom.objects.order_by('name')
    context = {
        'chat_list': chat_rooms,
    }
    return render(request, 'chat/index.html', context)

def chat_room(request, chat_room_id):
    chat = ChatRoom.objects.get(slug=chat_room_id)
    chat_rooms = ChatRoom.objects.order_by('name')
    context = {
        'chat': chat,
        'chat_rooms': chat_rooms,
    }
    return render(request, 'chat/chat_room.html', context)
