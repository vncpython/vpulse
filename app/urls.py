from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('doctor.html',views.doctor),
    path('home.html',views.home),
    path('statistics.html',views.statistics),
    path('pharmacy.html',views.pharmacy),
    

]