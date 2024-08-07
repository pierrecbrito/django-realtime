from django.contrib import admin
from django.urls import path
from .views import index, chats, chat, logout

urlpatterns = [
    path('', view=index, name="index"),
    path('chats/', view=chats, name="chats"),
    path('chat/<int:grupo>/', view=chat, name="chat"),
    path('logout/', view=logout, name="logout")
]