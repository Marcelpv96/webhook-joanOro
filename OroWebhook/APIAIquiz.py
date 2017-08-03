import json
import random
from models import LastQuestion, Question
from wordsLanguages import words

language = "English"


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
    LastQuestionAnswer = checkQuestion()
    if LastQuestionAnswer == optionChoosed:
        result = words[language]["Correct"]
    else:
        result = words[language]["Incorrect"][0] + \
            LastQuestionAnswer + words[language]["Incorrect"][1]

    print topic
    questionGenerated = chooseQuestionByTopic(topic)
    print questionGenerated
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
