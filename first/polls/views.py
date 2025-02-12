from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("""
        <div style="font-family: Arial, sans-serif; background-color: #f0f0f0; 
                    color: #333; padding: 20px; text-align: center;">
            <h1 style="color: #007bff;">Hi i am Jaya Nanda Prabhas.</h1>
            <p style="font-size: 18px;">My roll number is 238W1A12G5</p>
        </div>
        """)