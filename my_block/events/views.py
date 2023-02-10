from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import NewsForms
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# def home_event(request):
#     return render(request, 'events/home_event.html')


# Create your views here.

class HomeeEents(ListView):
    model = EventsBlonck
    template_name = 'events/home_events_list.html'
    context_object_name = 'events'
    extra_context = {'title': 'Главное'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return EventsBlonck.objects.filter(is_published=True)


class EvetnByCatory(ListView):
    model = EventsBlonck
    template_name = 'events/home_events_list.html'
    context_object_name = 'events'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return EventsBlonck.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewEvetns(DetailView):
    model = EventsBlonck
    context_object_name = 'event_item'
    # template_name = 'events/eventsblonck_detail.html'
    # pk_url_kwarg = 'event_id'


class CreateEvent(CreateView):
    form_class = NewsForms
    template_name = 'events/add_event.html'
    # success_url = reverse_lazy('event_home')

# def home_event(request):
#     events = EventsBlonck.objects.all()
#     context = {
#         'events': events,
#         'title': 'Список',
#     }
#     # res = '<<h1>Записи</h1>'
#     # for event in events:
#     #     res += f'<div>\n<p>{event}</p>\n</div>'
#     return render(request, template_name='events/home_event.html', context=context)
#
#
# def get_category(request, category_id):
#     events = EventsBlonck.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'events/index.html', {'events': events, 'category': category})


# def view_event(request, event_id):
#     # event_item = EventsBlonck.objects.get(pk=event_id)
#     event_item = get_object_or_404(EventsBlonck, pk=event_id)
#     return render(request, 'events/view_event.html', {'event_item': event_item})


# def add_event(request):
#     if request.method == 'POST':
#         form = NewsForms(request.POST)
#         if form.is_valid():
#             event = form.save()
#             return redirect(event)
#     else:
#         form = NewsForms()
#     return render(request, 'events/add_event.html', {'form': form})
