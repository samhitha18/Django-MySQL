from dataclasses import fields
from django.contrib import admin

# Register your models here.

from .models import employees

# admin.site.register(employees)

class employeesAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'department']
admin.site.register(employees, employeesAdmin)