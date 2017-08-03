import random
#from Lenguage import LenguageWords
from models import LastQuestion, Question

default_lenguage = ""

def createWebhookAnswer(answer):
    return {
        "speech": answer,
        "displayText": answer,
        "source": "API.AI-test-simple-Quiz"
    }


def JSONtoQuestion(jsonData):
    return "The question is " + jsonData['Question'] \
        + ", Option A " + jsonData['AnswerA'] \
        + ", Option B " + jsonData['AnswerB'] \
        + ", or Option C " + jsonData['AnswerC']


def checkQuestion():
    lastQuestion = LastQuestion.objects.order_by('-id')[0]
    LastQuestion.objects.order_by('-id')[0].delete()
    return lastQuestion.correct()


def chooseQuestionByTopic(topic):
    n = random.randint(0, Question.objects.filter(
        QuestionTopic=topic).count() - 1)
    questionByTopicValues = Question.objects.filter(
        QuestionTopic=topic).order_by('id').values()
    questionByTopic = Question.objects.filter(
        QuestionTopic=topic).order_by('id')[n]
    question = LastQuestion(question=questionByTopic)
    question.save()
    questionValue = JSONtoQuestion(questionByTopicValues[n])
    return questionValue


def generateQuestionChoosedTest(topic):
    questionGenerated = chooseQuestionByTopic(topic)
    return createWebhookAnswer(questionGenerated)


def generateQuestion(topic, optionChoosed):
    LastQuestion = checkQuestion()
    if LastQuestion == optionChoosed:
        result = 'Correct Answer now  '
    else:
        result = 'Incorrect Answer, the correct was ' + LastQuestion + ' now   '
    questionGenerated = chooseQuestionByTopic(topic)
    return createWebhookAnswer(result + questionGenerated)


def generateResultAnswer(action, optionChoosed):
    result = createWebhookAnswer("ERRROR")
    if action.split('_')[0] == 'start':
        result = createWebhookAnswer(
            "Ok, Say a topic for start with the Questions, If you don't know which topics are available say Topic List for more information.")
    if action.split('_')[0] == 'test':
        result = generateQuestionChoosedTest(action.split('_')[-1])
    if action.split('_')[0] == 'answer':
        result = generateQuestion(action.split('_')[-1], optionChoosed)
    return result


def userChoosed(request_data):
    user_answered = request_data['result']['resolvedQuery'].split()[-1]
    return user_answered
