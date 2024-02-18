from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from .models import User_info

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        identifier = hashlib.md5((email + phone).encode()).hexdigest()
        
        
        if User_info.objects.filter(identifier=identifier).exists():
            return JsonResponse({'error': 'You have already submitted this form.'}, status=400)
        
        
        user_info = User_info(name = name, email=email, phone=phone, identifier=identifier)
        user_info.save()
        
        return JsonResponse({'message': 'Form submitted successfully.'})


