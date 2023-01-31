from django.shortcuts import render,redirect
from .models import Profile,Friend,ChatMessage
from .forms import ChatMessageForm
from django.http import JsonResponse
import json

def index(request):
    user=request.user.profile
    friends=user.friends.all()
    context={"user":user,"friends":friends}
    return render(request,"mychatapp/index.html",context)


def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user =request.user.profile
    profile=Profile.objects.get(id=friend.profile.id)
    chats=ChatMessage.objects.all()
    print(chats[0].msg_sender.soyad)
    form=ChatMessageForm()
    if request.method=="POST":
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message=form.save(commit=False)
            chat_message.msg_sender=user 
            chat_message.msg_receiver=profile
            chat_message.save()
            idpk=friend.profile.id
            
            return redirect("detail",pk=idpk)
    context={"friend":friend,"form":form,"user":user,"profile":profile,"chats":chats}
    return render(request,"mychatapp/detail.html",context)


def sentMessages(request,pk):
    user=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    profile=Profile.objects.get(id=friend.profile.id)
    data=json.loads(request.body)
    new_chat=data["msg"]
    new_chat_message=ChatMessage.objects.create(body=new_chat,msg_sender=user,msg_receiver=profile,seen=False)
    print(new_chat)
    return JsonResponse(new_chat_message.body,safe=False)