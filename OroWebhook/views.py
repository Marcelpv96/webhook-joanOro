import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers

def create_answer(answer):
    return {
                "speech": answer,
                "displayText": answer,
                "source": "API.AI-test-simple-Quiz"
            }



def checkQuestion(action):
    return True

def generateAnswerChoosedTest(action):
    if action == 'choosed_test_Nasa':
        return create_answer("Correct Answer Nasa, : .......")
    if action == 'choosed_test_Family':
        return create_answer("Correct Answer family, : .......")
    if action == 'choosed_test_Random':
        return create_answer("Correct Answer Random, : .......")

def generateAnswer(action):
    if action  == 'choosed_answer_Family':
        return create_answer("Correct Answer family, Now the question is: .......")
    if action == 'choosed_answer_Random':
        return create_answer("Correct Answer random, Now the question is: .......")
    if action == 'choosed_answer_Nasa':
        return create_answer("Correct Answer nasa, Now the question is: .......")

def getResult(action):
    try:
        if action.startswith('start'):
            result = create_answer("Choose the test, say a topic or say Random for a random test.")
        if action.startswith('choosed_test'):
            result = generateAnswerChoosedTest(action)
        if action.startswith('choosed_answer'):
            result = generateAnswer(action)
    except :
        result = create_answer("ERRROR")
    return result


@csrf_exempt
@require_POST
def webhook(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    result = getResult(action)
    return JsonResponse(result)
