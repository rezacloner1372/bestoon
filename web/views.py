
from lib2to3.pgen2 import token
from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income, Token, User
from datetime import date, datetime
# Create your views here.


@csrf_exempt
def submit_income(request):

    this_token = request.POST.get('token')
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(text=request.POST.get(
        'text'), amount=request.POST.get('amount'), date=date, user=this_user)

    return JsonResponse({'status': 'ok'},
                        encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):

    this_token = request.POST.get('token')
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(text=request.POST.get(
        'text'), amount=request.POST.get('amount'), date=date, user=this_user)

    return JsonResponse({'status': 'ok'},
                        encoder=JSONEncoder)
