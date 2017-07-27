import copy
import json
import datetime
import random
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


def checkQuestion(optionChoosed):
    lastQuestion = LastQuestion.objects.filter(testfield=12).order_by('-id')[0]
    LastQuestion.objects.filter(testfield=12).order_by('-id')[0].delete()
    return lastQuestion.correct() == optionChoosed


def genetareQuestion(topic):
    return create_answer('QUESTION :' + topic)


def generateQuestionChoosedTest(action):
    return genetareQuestion('action')


def generateQuestion(topic):
    if checkQuestion():
        result = 'Correct Answer, now the question is : '
        questionGenerated = generateQuestion(topic)
        lastQuestion = LastQuestion(question=questionGenerated)
    else:
        result = 'Incorrect Answer, now the question i : '

    return create_answer(result + ' ...')


def getResult(action):
    try:
        if action.split('_')[0] == 'start':
            result = create_answer(
                "Choose the test, say a topic or say Random for a random test.")
        if action.split('_')[0] == 'test':
            result = generateQuestionChoosedTest(action.split('_')[-1])
        if action.split('_')[0] == 'answer':
            result = generateQuestion(action.split('_')[-1])
    except:
        result = create_answer("ERRROR")
    return result


def userChoosed(request_data):
    user_answered = request_data['result']['resolvedQuery'].split()
    if 'A' in user_answered:
        return 'A'
    if 'B' in user_answered:
        return 'B'
    if 'C' in user_answered:
        return 'C'
    return 'NO ANSWER'


@csrf_exempt
@require_POST
def webhook(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    optionChoosed = userChoosed(request_data)
    result = getResult(action)
    return JsonResponse(result)
