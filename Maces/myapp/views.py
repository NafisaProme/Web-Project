from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User_info
import hashlib
from django.contrib import messages

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        identifier = hashlib.md5((email + phone).encode()).hexdigest()
        
        user_info1 = User_info.objects.filter(email=email)
        user_info2 = User_info.objects.filter(phone=phone)
        
        if user_info1.exists() or user_info2.exists():
            messages.error(request, 'Email and phone combination must be unique.')
        else:
            user_info = User_info(name=name, email=email, phone=phone, identifier=identifier)
            user_info.save()
            messages.success(request, 'Form submitted successfully.')
        
    return render(request, 'form.html')
