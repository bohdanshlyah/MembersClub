import re

from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import get_list_of_members, add_member

def show_members_list(request):
    return render(request,'index.html', {'members': get_list_of_members()})

def new_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        try:
            add_member(name, email)
        except ValidationError as e :
            messages.warning(request, e.message)


        return redirect('all_members')
    return render(request, 'index.html', {})