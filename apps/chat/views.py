from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    context = {
        'sections': [{
            'link': reverse('chat', args=(1,)),
            'name': 'Литература',
            'image_url': 'images/chat/open-book.svg',
        }, {
            'link': reverse('chat', args=(2,)),
            'name': 'Проект',
            'image_url': 'images/chat/idea.svg',
        }, {
            'link': reverse('chat', args=(3,)),
            'name': 'Тех. помощь',
            'image_url': 'images/chat/repair.svg',
        }, {
            'link': reverse('chat', args=(4,)),
            'name': 'Теория',
            'image_url': 'images/chat/knowledge.svg',
        }, {
            'link': reverse('chat', args=(5,)),
            'name': 'Флудилка',
            'image_url': 'images/chat/chat.svg',
        }]
    }
    return render(request, 'chat/index.html', context=context)


def chat_view(request, chat_id):
    return render(request, 'chat/chat.html', context={'chat_id': chat_id})
