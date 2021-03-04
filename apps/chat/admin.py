from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import SectionForm
from .models import *


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class ConversationInline(admin.TabularInline):
    model = Conversation
    extra = 0
    readonly_fields = ('text', 'user',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    inlines = (ConversationInline,)
    form = SectionForm


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = ('text', 'user',)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'user', 'created_at', 'modified_at',)
    list_filter = ('section', 'user',)
    search_fields = ('text', 'section__title',)
    readonly_fields = ('user',)
    inlines = (MessageInline,)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'modified_at',)
    list_filter = ('conversation', 'conversation__section', 'user',)
    search_fields = ('text', 'conversation__text',
                     'conversation__section__title',)
    readonly_fields = ('user',)
