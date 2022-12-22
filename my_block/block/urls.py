from django.urls import path
from .views import *


urlpatterns = [
    path('', counterparties_block, name='counterparties_block'),
    path('records/', records, name='records')
]