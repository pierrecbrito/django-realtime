from django.contrib import admin
from django.urls import path, include
from .views import index, chats, chat

urlpatterns = [
    path('', view=index, name="index"),
    path('chats/', view=chats, name="chats"),
    path('chat/<int:grupo>/', view=chat, name="chat")
]