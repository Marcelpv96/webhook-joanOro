import json
import random
from models import LastQuestion, Question
from wordsLanguages import words

language = "Spanish"


def createWebhookAnswer(answer):
    return {
        "speech": answer,
        "displayText": answer,
        "source": "API.AI-test-simple-Quiz"
    }


def JSONtoQuestion(jsonData):
    return words[language]["Question"] + jsonData['Question'] \
        + words[language]["OptionA"] + jsonData['AnswerA'] \
        + words[language]["OptionB"] + jsonData['AnswerB'] \
        + words[language]["OptionC"] + jsonData['AnswerC']

def questionToString(question):
    return words[language]["Question"] + question.Question \
        + words[language]["OptionA"] + question.AnswerA \
        + words[language]["OptionB"] + question.AnswerB \
        + words[language]["OptionC"] + question.AnswerC
def checkQuestion():
    lastQuestion = LastQuestion.objects.order_by('-id')[0]
    return lastQuestion.correct()


def chooseQuestionByTopic(topic):
    n = random.randint(0, Question.objects.filter(
        QuestionTopic=topic).count() - 1)
    questionByTopicValues = Question.objects.filter(
        QuestionTopic=topic).order_by('id').values()
    questionByTopic = Question.objects.filter(
        QuestionTopic=topic).order_by('id')[n]
    LastQuestion.objects.order_by('-id')[0].delete()
    question = LastQuestion(question=questionByTopic,tries="0")
    question.save()
    questionValue = JSONtoQuestion(questionByTopicValues[n])
    return questionValue


def generateQuestionChoosedTest(topic):
    questionGenerated = chooseQuestionByTopic(topic)
    return createWebhookAnswer(questionGenerated)


def generateQuestion(topic, optionChoosed):
    tries = LastQuestion.objects.order_by('-id')[0].tries
    LastQuestionAnswer = checkQuestion()
    print "hola"
    print LastQuestionAnswer
    print optionChoosed
    if LastQuestionAnswer.split(',')[0] == optionChoosed.upper():
        result = words[language]["Correct"]
        questionGenerated = chooseQuestionByTopic(topic)
    elif tries == "0":
        result = "Incorrect answer, another try. "
        questionGenerated= questionToString(LastQuestion.objects.order_by('-id')[0].question)
        q = LastQuestion(question=LastQuestion.objects.order_by('-id')[0].question,tries="1")
        q.save()
        tries = LastQuestion.objects.order_by('-id')[0].tries

    elif tries == "1":
        result = words[language]["Incorrect"][0] + \
            LastQuestionAnswer + words[language]["Incorrect"][1]
        questionGenerated = chooseQuestionByTopic(topic)

    return createWebhookAnswer(result + questionGenerated)


def getAction(action, optionChoosed):
    result = createWebhookAnswer("ERRROR")
    if action.split('_')[0] == 'start':
        result = createWebhookAnswer(words[language]["Starting"])
    if action.split('_')[0] == 'test':
        result = generateQuestionChoosedTest(action.split('_')[-1])
    if action.split('_')[0] == 'answer':
        result = generateQuestion(action.split('_')[-1], optionChoosed)
    return result


def userChoosed(request_data):
    user_answered = request_data['result']['resolvedQuery'].split()[-1]
    return user_answered
