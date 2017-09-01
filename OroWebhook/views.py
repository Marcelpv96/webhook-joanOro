import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse

import APIAIquiz as quiz


@csrf_exempt
@require_POST
def webhookOro(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    quiz.language = "English"
    optionChoosed = quiz.userChoosed(request_data)
    result = quiz.getAction(action, optionChoosed)
    return JsonResponse(result)


@csrf_exempt
@require_POST
def webhookSalamanca(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    quiz.language = "English"
    optionChoosed = quiz.userChoosed(request_data)
    result = quiz.getAction(action, optionChoosed)
    return JsonResponse(result)
