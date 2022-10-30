from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models.audit import Audit
from core.models.pinpad import PinPadStatus


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def check_password(request, input):
    password = PinPadStatus.get_pinpad_password()
    unlock = password == input
    response = {"unlock": unlock}
    Audit.add_audit(unlock)
    return JsonResponse(response, status=200)


@csrf_exempt
def status(request):
    unlock = Audit.is_unlocked()
    response = {"unlock": unlock}
    return JsonResponse(response, status=200)
