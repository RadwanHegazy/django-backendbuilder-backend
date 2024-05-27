from django.contrib import admin
from .models import User, Tenant

@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ('full_name','email','id',)

@admin.register(Tenant)
class TenantPanel (admin.ModelAdmin) : 
    list_display = ('user','name','id',)