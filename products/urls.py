from django.urls import path
from . import views 

urlpatterns = [
    path('Products',views.product , name = 'product') ,
    path('',views.products , name = 'products') ,

]
