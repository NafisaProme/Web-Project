from django.urls import path
from .views import submit_form

urlpatterns = [
    path('submit_form/', submit_form, name='submit_form'),
]
