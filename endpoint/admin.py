from django.contrib import admin
from .models import Endpoint

@admin.register(Endpoint)
class EndpointPanel (admin.ModelAdmin) : 
    list_display = ('tenant','name',)