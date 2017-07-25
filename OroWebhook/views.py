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

def getResult(action):
    try:
        if action == 'start_test':
            result = create_answer("Choose the test, say a topic or say Random for a random test.")
        if action == 'choosed_test':
            result = create_answer("Ok, the Question now is: ........")
        if action == 'answer_choosed':
            if checkQuestion(action):
                result = create_answer("Correct Answer, Now the question is: .......")
            else:
                result = create_answer("Incorrect Answer, the correct is: ......, new Question : ......")
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
