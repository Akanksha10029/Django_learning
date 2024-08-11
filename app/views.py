from django.shortcuts import render
from .models import ChaiVariety, store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_app(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'app/all_app.html',{'chais': chais})

def order(request):
    return render(request, 'app/order_app.html')

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "app/chai_detail.html", {"chai":chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        # store_name = request.POST['store_name']
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_varriety = form.cleaned_data['chai_variety']
            stores = store.objects.filter(ChaiVarieties= chai_varriety)
    else:
        form = ChaiVarietyForm()
        
    return render(request, 'app/chai_stores.html',{'stores':stores, 'form':form})