from django.shortcuts import render



def home_event(request):
    return render(request, 'events/home_event.htlm')
# Create your views here.
