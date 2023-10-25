# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
@csrf_exempt
def formulaire_message(request):
    return render(request, 'napi/formulaire_message.html')

@csrf_exempt

def traiter_message(request):
    if request.method == 'POST':
        contenu = request.POST.get('contenu')

        # Traitement du message 

        # Enregistrement du message dans la base de données distante
        nouveau_message = Message(contenu=contenu)
        nouveau_message.save(using='default')  # 'default' correspond au nom de la base de données dans DATABASES

        response = JsonResponse({'message': 'Message traité avec succès'})

        # Autoriser toutes les origines 
        response["Access-Control-Allow-Origin"] = "*"

        return response

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
