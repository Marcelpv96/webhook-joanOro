import copy, json, datetime, random
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers

from models import LastQuestion


def create_answer(answer):
    return {
                "speech": answer,
                "displayText": answer,
                "source": "API.AI-test-simple-Quiz"
            }



def checkQuestion():
    #lastQuestion = LastQuestion.objects.filter(testfield=12).order_by('-id')[0]
    return True

def genetareQuestion(topic):
    return create_answer('QUESTION :'+topic)

def generateAnswerChoosedTest(action):
    return genetareQuestion('action')

def generateAnswer(action):
    if checkQuestion():
        result = 'Correct Answer, now the question is : '
    else:
        result = 'Incorrect Answer, now the question i : '

    return create_answer(result + ' ...')


def getResult(action):
    try:
        if action.split('_')[0] == 'start':
            result = create_answer("Choose the test, say a topic or say Random for a random test.")
        if action.split('_')[0] == 'choosed':
            result = generateAnswerChoosedTest(action.split('_')[-1])
        if action.split('_')[0] == 'answer':
            result = generateAnswer(action.split('_')[-1])
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
