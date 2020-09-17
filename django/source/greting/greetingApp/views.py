
from django.shortcuts import render, HttpResponse

# Create your views here

def greeting(request):
    return HttpResponse('장고 프레임워크')

def hi(request):
    return render(request, 'greeting/msg.html')

