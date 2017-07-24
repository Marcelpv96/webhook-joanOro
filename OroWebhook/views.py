import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers


@require_POST
def webhook(request):
    request_data = json.loads(request)[0]
    try:
        result = {
            "speech": request_data['result']['action'],
            "displayText": request_data['result']['action'],
            "source": "API.AI-test-simple-Quiz"
        }
    except KeyError:
        result = {
            "speech": "ERROR",
            "displayText": "ERROR",
            "source": "API.AI-test-simple-Quiz"
        }
    return JsonResponse(result)
