from django.urls import path
from .views import *


urlpatterns = [
    path('', home_block, name='home_lock')
]