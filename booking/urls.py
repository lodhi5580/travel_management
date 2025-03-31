from django.urls import path
from .views import BusListCreateView, RouteListCreateView, TicketListCreateView, UserTicketsView

urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='bus-list-create'),
    path('routes/', RouteListCreateView.as_view(), name='route-list-create'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('user-tickets/', UserTicketsView.as_view(), name='user-tickets'),
]
