# urls.py

from django.urls import path
from .views import traiter_message, formulaire_message

urlpatterns = [
    path('traiter_message/', traiter_message, name='traiter_message'),
    path('formulaire_message/', formulaire_message, name='formulaire_message'),
]
