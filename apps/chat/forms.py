from django import forms

from apps.chat.models import Conversation, Message, Section
from apps.chat.svg_image_field import SvgAndImageFormField


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ('text',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
