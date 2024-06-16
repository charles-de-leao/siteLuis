from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('sobre', sobre, name="sobre"),
    path('shows', shows, name="shows"),
    path('contato', contato, name="contato"),
]