from django.contrib import admin
from .models import Bus, Route, Ticket

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Ticket)
