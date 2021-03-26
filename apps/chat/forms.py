from django import forms

from apps.chat.models import Section
from apps.chat.svg_image_field import SvgAndImageFormField


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }
