import copy, json, datetime
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import WebhookTransaction


@csrf_exempt
@require_POST
def webhook(request):

    return {
        "speech": "a",
        "displayText": "a",
        "source": "API.AI-test-simple-Quiz"
    }
