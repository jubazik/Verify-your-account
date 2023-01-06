from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# def home_event(request):
#     return render(request, 'events/home_event.html')


# Create your views here.


def home_event(request):
    events = EventsBlonck.objects.all()
    categorys = Category.objects.all()
    context = {
        'events': events,
        'title': 'Список',
        'categorys': categorys
    }
    # res = '<<h1>Записи</h1>'
    # for event in events:
    #     res += f'<div>\n<p>{event}</p>\n</div>'
    return render(request, template_name='events/home_event.html', context=context)


def get_category(request, category_id):
    events = EventsBlonck.objects.filter(category_id=category_id)
    categorys = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'events/index.html', {'events': events, 'categorys': categorys, 'category': category})
