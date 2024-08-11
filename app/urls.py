from django.urls import path
from .import views


# localhost:8000/app
# localhost:8000/app/order

urlpatterns = [
    path('', views.all_app,name='all_app'),
    path('order/', views.order,name='app_order'),
    path('<int:chai_id>/', views.chai_detail, name="chai_detail"),
    path('chai_stores/', views.chai_store_view, name="chai_stores"),
]
    

