from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>vk is the best batsman for rcb</h1>')

def abd(request):
    return render(request,'abd.html')