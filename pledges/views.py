from django.shortcuts import render
from django.http import HttpResponse
from .models import Pledge

def add_pledge(request):
    pledge = Pledge()
    pledge.save()
    return HttpResponse("Pledge added successfully")
#
# The add_pledge function is a view function that creates a new Pledge object and saves it to the database.