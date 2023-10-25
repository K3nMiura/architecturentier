# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
@csrf_exempt
def formulaire_message(request):
    return render(request, 'napi/formulaire_message.html')

@csrf_exempt
# Utilisé pour exclure cette vue spécifiquement de la protection CORS (à utiliser avec prudence)
def traiter_message(request):
    if request.method == 'POST':
        contenu = request.POST.get('contenu')

        # Traitement du message (à adapter selon tes besoins)

        # Enregistrement du message dans la base de données distante
        nouveau_message = Message(contenu=contenu)
        nouveau_message.save(using='default')  # 'default' correspond au nom de la base de données dans DATABASES

        response = JsonResponse({'message': 'Message traité avec succès'})

        # Autoriser toutes les origines (à ajuster en fonction de tes besoins)
        response["Access-Control-Allow-Origin"] = "*"

        return response

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
