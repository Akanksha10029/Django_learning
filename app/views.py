from django.shortcuts import render

# Create your views here.
def all_app(request):
    return render(request, 'app/all_app.html')

def order(request):
    return render(request, 'app/order_app.html')