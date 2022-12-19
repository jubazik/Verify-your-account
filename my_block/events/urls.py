from django.urls import path
from .views import *


urlpatterns = [
    path('', home_event, name='event'),
    path('get_all/', get_all),
]