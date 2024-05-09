
from django.urls import path
from .import views
urlpatterns = [
        path('add_pledge/', views.add_pledge, name='add_pledge'),
        ]       

