"""EV_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
   path('',views.index,name='index'),
   path('index/',views.index,name='index'),  
   
   path('register/',views.register,name='register'), 
   path('login/',views.login,name='login'),
   path('profile/',views.profile,name='profile'),
   path('home/',views.home,name='home'),
   
   path('ser_register/',views.ser_register,name='ser_register'),
   path('ser_login/',views.ser_login,name='ser_login'),
   path('ser_profile/',views.ser_profile,name='ser_profile'),
   path('ser_home/',views.ser_home,name='ser_home'),
   
   path('tutorial/',views.tutorial,name='tutorial'),
   path('feedback/',views.feedback,name='feedback'),
   path('reviews/',views.reviews,name='reviews'),
   
   path('stations/',views.stations,name='stations'),
   path('services/',views.services,name='services'),
   
   path('add_station/',views.add_station,name='add_station'),
   path('add_service/',views.add_service,name='add_service'),
   
   path('payment/<int:id>',views.payment,name='payment'),
   path('payments/<int:id>',views.payments,name='payments'),
   path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
   
   path('admin_home/',views.admin_home,name='admin_home'),
   path('admin_reg/',views.admin_reg,name='admin_reg'),
   path('admin_login/',views.admin_login,name='admin_login'),
   
   path('bookings/',views.bookings,name='bookings'),
   path('orders/',views.orders,name='orders'),
   
   path('stations_search/',views.stations_search,name='search'),
   path('services_search/',views.services_search,name='search'),

   path('users_list/',views.users_list,name='uers_list'),
   path('delete_record1/<int:id>',views.delete_record1,name="delete_record1"),

   path('stations_list/',views.stations_list,name='stations_list'),
   path('delete_record2/<int:id>',views.delete_record2,name="delete_record2"),

   path('services_list/',views.services_list,name='services_list'),
   path('delete_record3/<int:id>',views.delete_record3,name="delete_record3"),
   
   path('feedback_list/',views.feedback_list,name='feedback_list'),
   path('delete_record4/<int:id>',views.delete_record4,name="delete_record4"),
   
   path('payments_list/',views.payment_list,name='payment_list'),
   path('delete_record5/<int:id>',views.delete_record5,name="delete_record5"),
   
   path('view_station/', views.view_stations, name='view_stations'),
   path('update_status/', views.update_status, name='update_status'),
   path('delete_station/<int:id>',views.delete_station,name="delete_station"),
   
   path('view_service/', views.view_services, name='view_services'),
   path('update_service/', views.update_service, name='update_service'),
   path('delete_service/<int:id>',views.delete_service,name="delete_service"),
   
    
]
