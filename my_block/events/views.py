from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_event(request):
    return render(request, 'events/home_event.html')


# Create your views here.


def get_all(request):
    events = EventsBlonck.objects.all()
    context = {
        'events': events,
        'title':'список контрагентов'
    }
    # res = '<<h1>Записи</h1>'
    # for event in events:
    #     res += f'<div>\n<p>{event}</p>\n</div>'
    return render(request, template_name='events/home_event.html', context= context)
