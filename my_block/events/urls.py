from django.urls import path
from .views import *

urlpatterns = [
    # path('', home_event, name='event_home'),
    path('', HomeeEents.as_view(), name='event_home'),
    path('category/<int:category_id>/', EvetnByCatory.as_view(), name='category'),
    path('event/<int:pk>/', ViewEvetns.as_view(), name='view_event'),
    # path('event/<int:event_id>/', view_event, name='view_event'),
    path('event/edd-events/', CreateEvent.as_view(), name='add_event'),
    # path('event/edd-events/', add_event, name='add_event'),
]
