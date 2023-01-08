from django.urls import path
from .views import *


urlpatterns = [
    path('', counter, name='counter'),
    path('records/', records, name='record'),
    # path('bl/', blog_all, name='blog'),
    path('records/<int:record_id>/', get_record_id, name='get_record_id'),
    path('cunter/<int:coun_id>/', counterparties_category, name='count_id'),
]