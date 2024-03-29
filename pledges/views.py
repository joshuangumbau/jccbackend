from django.shortcuts import redirect
from django.contrib import messages

def add_pledge(request):
    if request.method == 'POST':

        messages.success(request, 'Pledge added successfully!')
        return redirect('add_pledge') 
    return redirect('admin:index')  