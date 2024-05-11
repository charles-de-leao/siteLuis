from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('', sobre, name="sobre"),
    path('', shows, name="shows"),
    path('', contato, name="contato"),
]