import copy
import json
import random
import datetime
import random
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers

from models import LastQuestion, QuestionTopic
from models import Question


def create_webhook_answer(answer):
    return {
        "speech": answer,
        "displayText": answer,
        "source": "API.AI-test-simple-Quiz"
    }


def checkQuestion(optionChoosed):
    lastQuestion = LastQuestion.objects.filter(testfield=12).order_by('-id')[0]
    LastQuestion.objects.filter(testfield=12).order_by('-id')[0].delete()
    return lastQuestion.correct() == optionChoosed


def chooseQuestionByTopic(topic):
    questionTopic = QuestionTopic.objects.filter(topic=topic)[0]
    questionsByTopic = Question.objects.filter(
        questionTopic=questionTopic).order_by('id')
    question = questionsByTopic[random.randint(0, len(questionsByTopic) - 1)]
    return question.generateSpeech()


def generateQuestionChoosedTest(topic):
    questionGenerated = generateQuestion(topic)
    lastQuestion = LastQuestion(question=questionGenerated)
    lastQuestion.save()
    return create_webhook_answer(questionGenerated)


def generateQuestion(topic,optionChoosed ):
    if checkQuestion(optionChoosed):
        result = 'Correct Answer, now the question is : '
    else:
        result = 'Incorrect Answer, now the question i : '
    questionGenerated = generateQuestion(topic)
    lastQuestion = LastQuestion(question=questionGenerated)
    lastQuestion.save()

    return create_webhook_answer(result + questionGenerated)


def getResult(action, optionChoosed):
    try:
        if action.split('_')[0] == 'start':
            result = create_webhook_answer(
                "Choose the test, say a topic or say Random for a random test.")
        if action.split('_')[0] == 'test':
            result = generateQuestionChoosedTest(action.split('_')[-1])
        if action.split('_')[0] == 'answer':
            result = generateQuestion(action.split('_')[-1],optionChoosed)
    except:
        result = create_webhook_answer("ERRROR")
    return result


def userChoosed(request_data):
    user_answered = request_data['result']['resolvedQuery'].split()
    return user_answered


@csrf_exempt
@require_POST
def webhook(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    optionChoosed = userChoosed(request_data)
    result = getResult(action, optionChoosed)
    return JsonResponse(result)
