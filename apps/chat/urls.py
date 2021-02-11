from django.urls import path

from apps.chat.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/<int:chat_id>/', chat_view, name='chat'),
]
