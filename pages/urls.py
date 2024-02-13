from django.urls import path 
from .views import HomePageView, AboutPageView , ProductIndexView , ProductShowView , ContactPageView , SuccessPageView , ProductCreateView

 

urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'), 
    path('about/', AboutPageView.as_view(), name='about'),
    path('productos/',ProductIndexView.as_view(), name='index'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contact/', ContactPageView.as_view(), name = "contact"),
    path('products/success', SuccessPageView.as_view(), name='success'),
    path('products/create', ProductCreateView.as_view(), name='form'),   

] 