import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import APAIquiz



@csrf_exempt
@require_POST
def webhookSalamanca(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    optionChoosed = APAIquiz.userChoosed(request_data)
    result = APAIquiz.generateResultAnswer(action, optionChoosed)
    return JsonResponse(result)

@csrf_exempt
@require_POST
def webhookOro(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    optionChoosed = APAIquiz.userChoosed(request_data)
    result = APAIquiz.generateResultAnswer(action, optionChoosed)
    return JsonResponse(result)
