from django.urls import path
from .views import *

urlpatterns = [
    path('', home_event, name='event_home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('event/<int:event_id>/', view_event, name='view_event'),
]
