
from django.urls import path
from .import views
urlpatterns = [
        path('create new pledge/', views.add_pledge, name = 'add_pledge'),
]