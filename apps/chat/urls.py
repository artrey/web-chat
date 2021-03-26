from django.urls import path

from apps.chat.views import index_view, section_view

urlpatterns = [
    path('', index_view, name='index'),
    path('chat/<int:section_id>/', section_view, name='section'),
]
