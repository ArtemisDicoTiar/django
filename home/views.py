from django.shortcuts import render, Http404
import datetime

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


class vip:
    key = 'Password 13asvo9ash349'

    def __init__(self):
        pass


def index(request):
    msg = 'My Message'
    Name = 'My name is John'
    k = vip.key
    cnt = -194

    date = datetime.datetime.today()
    lastname = 'KIM'
    temp_var = {
        'name': Name,
        'vip': {
            'key': k
        },
        'message': msg,
        'count': cnt,
        'it': {
            'name': 'DicoTiar'
        },
        'dataList': [
            {'name': 'DicoTiar',
             'id': 'w3ob2890'
             },
            {'name': 'Artemis',
             'id': 'qeb0923n'
             }
        ],
        'createDate': date,
        'lastName': lastname,
        'content': "<>'\"&@#SBAIOSDJAG"
    }

    return render(request, 'home/index.html', temp_var)