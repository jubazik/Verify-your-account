from django.shortcuts import render



def home_event(request):
    return render(request, 'events/home_event.html')
# Create your views here.
