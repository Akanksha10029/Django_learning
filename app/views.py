from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def all_app(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'app/all_app.html',{'chais': chais})

def order(request):
    return render(request, 'app/order_app.html')