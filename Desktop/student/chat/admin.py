from django.contrib import admin

# Register your models here.
"""Admin file for the chat app."""

from django.contrib import admin

from .models import ChatSession, ChatSessionMember, ChatSessionMessage


admin.site.register((ChatSession, ChatSessionMember, ChatSessionMessage))
