from django.urls import path

from apps.chat.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('chat/<int:section_id>/', section_view, name='section'),
]
