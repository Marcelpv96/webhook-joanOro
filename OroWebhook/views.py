import json
import random
import random
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from models import LastQuestion, Question


def createWebhookAnswer(answer):
    return {
        "speech": answer,
        "displayText": answer,
        "source": "API.AI-test-simple-Quiz"
    }

def JSONtoQuestion(jsonData):
    question = jsonData['Question']
    A = jsonData['AnswerA']
    B = jsonData['AnswerB']
    C = jsonData['AnswerC']
    return "The question is " +question+" Option A "+A+" Option B "+B+" or Option C "+C

def checkQuestion(optionChoosed):
    lastQuestion = LastQuestion.objects.order_by('-id')[0]
    LastQuestion.objects.order_by('-id')[0].delete()
    return lastQuestion.correct() == optionChoosed


def chooseQuestionByTopic(topic):
    n = random.randint(0,Question.objects.filter(QuestionTopic=topic).count()-1)
    questionByTopicValues = Question.objects.filter(
        QuestionTopic=topic).order_by('id').values()
    questionByTopic = Question.objects.filter(QuestionTopic=topic).order_by('id')[n]
    question = LastQuestion(question=questionByTopic)
    question.save()
    questionValue = JSONtoQuestion(questionByTopicValues[n])
    return questionValue


def generateQuestionChoosedTest(topic):
    questionGenerated = chooseQuestionByTopic(topic)
    return createWebhookAnswer(questionGenerated)


def generateQuestion(topic, optionChoosed):
    if checkQuestion(optionChoosed):
        result = 'Correct Answer, now the question is : '
    else:
        result = 'Incorrect Answer, now the question i : '

    print topic
    questionGenerated = chooseQuestionByTopic(topic)
    print questionGenerated
    return createWebhookAnswer(result + questionGenerated)


def getAction(action, optionChoosed):
    result = createWebhookAnswer("ERRROR")
    if action.split('_')[0] == 'start':
        result = createWebhookAnswer(
            "Choose the test, say a topic or say Random for a random test.")
    if action.split('_')[0] == 'test':
        result = generateQuestionChoosedTest(action.split('_')[-1])
    if action.split('_')[0] == 'answer':
        result = generateQuestion(action.split('_')[-1], optionChoosed)
    return result


def userChoosed(request_data):
    user_answered = request_data['result']['resolvedQuery'].split()[-1]
    return user_answered


@csrf_exempt
@require_POST
def webhook(request):
    request_data = json.loads(request.body)
    action = request_data['result']['action']
    optionChoosed = userChoosed(request_data)
    result = getAction(action, optionChoosed)
    return JsonResponse(result)
