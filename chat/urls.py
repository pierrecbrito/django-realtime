from django.contrib import admin
from django.urls import path, include
from .views import index, chats

urlpatterns = [
    path('', view=index, name="index"),
    path('chats/', view=chats, name="chats")
]