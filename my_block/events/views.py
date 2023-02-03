from django.shortcuts import render, get_object_or_404
from .models import *

# def home_event(request):
#     return render(request, 'events/home_event.html')


# Create your views here.


def home_event(request):
    events = EventsBlonck.objects.all()
    context = {
        'events': events,
        'title': 'Список',
    }
    # res = '<<h1>Записи</h1>'
    # for event in events:
    #     res += f'<div>\n<p>{event}</p>\n</div>'
    return render(request, template_name='events/home_event.html', context=context)


def get_category(request, category_id):
    events = EventsBlonck.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'events/index.html', {'events': events, 'category': category})


def view_event(request, event_id):
    # event_item = EventsBlonck.objects.get(pk=event_id)
    event_item = get_object_or_404(EventsBlonck,pk=event_id)
    return render(request, 'events/view_event.html', {'event_item': event_item})
