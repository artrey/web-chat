from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.models import User


class Section(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/sections')

    def __str__(self):
        return f'{self.id}: {self.title}'


class Conversation(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                related_name='conversations')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.text} | {self.created_at}'


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE,
                                     related_name='messages')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
