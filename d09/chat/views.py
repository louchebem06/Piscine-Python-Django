from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, CustomUser, Message

@login_required(login_url='/account')
def index(request):
    rooms = ChatRoom.objects.all()
    rooms = rooms.values()
    return render(request, 'chat/index.html', {"rooms" : rooms})

@login_required(login_url='/account')
def room(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    messages = Message.objects.filter(room=room).order_by('-id')
    messages = messages.values()[:3]
    msgs = list()
    for msg in reversed(messages):
        message = msg['msg']
        user = CustomUser.objects.get(id=msg["user_id"]).username
        msgs.append({"msg": message, "user": user})
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages' : msgs
    })
