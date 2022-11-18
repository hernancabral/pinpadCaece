from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models.audit import Audit
from core.models.pinpad import PinPadStatus
from pinpad import settings


def index(request):
    return render(request, 'index.html')


@login_required
def change_password_view(request):
    return render(request, 'change_password.html')


@login_required
@csrf_exempt
def change_password(request, input):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    PinPadStatus.set_pinpad_password(input)
    return JsonResponse({}, status=200)


@csrf_exempt
def check_password(request, input):
    password = PinPadStatus.get_pinpad_password()
    unlock = password == input
    Audit.add_audit(unlock)
    if unlock:
        status_code = 200
    else:
        status_code = 403
    return JsonResponse({}, status=status_code)


@csrf_exempt
def status(request):
    unlock = Audit.is_unlocked()
    if unlock:
        status_code = 200
    else:
        status_code = 403
    return JsonResponse({}, status=status_code)
