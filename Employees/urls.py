from django.urls import path
from . import views
urlpatterns = [path('employees/',views.people,name="Employees"),]