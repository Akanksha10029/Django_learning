from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_app(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'app/all_app.html',{'chais': chais})

def order(request):
    return render(request, 'app/order_app.html')

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "app/chai_detail.html", {"chai":chai})