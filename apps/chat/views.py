from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from apps.chat.models import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'auth/login.html')


def index_view(request):
    print(request.user)
    context = {
        'sections': Section.objects.all(),
    }
    return render(request, 'chat/index.html', context=context)


def section_view(request, section_id):
    if request.method == 'POST':
        message = request.POST.get('message')
        Conversation.objects.create(text=message, section_id=section_id, user_id=1)

    conversations = Conversation.objects.filter(section_id=section_id)
    context = {
        'section_id': section_id,
        'conversations': conversations,
    }
    return render(request, 'chat/section.html', context=context)
