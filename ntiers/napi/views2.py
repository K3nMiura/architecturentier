# views.py

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
@csrf_exempt
def formulaire_message(request):
    return render(request, 'napi/formulaire_message.html')

@csrf_exempt
def traiter_message(request):
    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        
        # Traitement du message (à adapter selon tes besoins)

        # Enregistrement du message dans la base de données distante
        nouveau_message = Message(contenu=contenu)
        nouveau_message.save(using='default')  # 'default' correspond au nom de la base de données dans DATABASES

        # Récupération de la page d'origine
        referer = request.META.get('HTTP_REFERER')

        if referer:
            # Utilisation de JavaScript pour effectuer la redirection côté client
            return HttpResponseBadRequest(f'<script>window.location.replace("{referer}");</script>')
        else:
            # Redirection par défaut (à adapter selon tes besoins)
            return redirect('https://10.8.128.156')  # Remplace 'accueil' par le nom de ta vue ou l'URL souhaitée

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
# Create your views here.
