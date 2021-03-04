from django.shortcuts import render

from apps.chat.models import *


def index_view(request):
    context = {
        'sections': Section.objects.all(),
    }
    return render(request, 'chat/index.html', context=context)


def section_view(request, section_id):
    text = request.GET.get('text')
    if text:
        Conversation.objects.create(text=text, section_id=section_id, user_id=1)

    conversations = Conversation.objects.filter(section_id=section_id)
    context = {
        'section_id': section_id,
        'conversations': conversations,
    }
    return render(request, 'chat/section.html', context=context)
