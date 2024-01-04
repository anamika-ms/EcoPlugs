from django.shortcuts import render,redirect
from . models import reg,service_reg,feed,station,service,pay,super_user

# Create your views here.

import random
import smtplib
import razorpay #import this
from django.conf import settings
from django.http import JsonResponse #import this
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #import this
from django.http import HttpResponseBadRequest #import this
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def index(request):
    return render(request,'index.html')

# user views

def home(request):
    return render(request,'home.html')


def register(request):
   if request.method =='POST':
      fname = request.POST.get('rfname')
      phone = request.POST.get('rcontact')
      email = request.POST.get('remail')
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      reg(fullname=fname,contact=phone,email=email,username=uname,password=passw).save()
      return render(request,'login.html')
   else:
      return render(request,'register.html')


def login(request):
   if request.method=='POST':
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      cr = reg.objects.filter(username=uname,password=passw)
      if cr:
         details = reg.objects.get(username=uname, password = passw)
         username = details.username
         request.session['cs']=username

         return render(request,'home.html')
      else:
         message="Invalid Username Or Password"
         return render(request,'login.html',{'me':message})
   else: 
      return render(request,'login.html')


def profile(request):
   c=request.session['cs']
   cr=reg.objects.get(username=c)
   pfname=cr.fullname
   pcontact=cr.contact
   pemail=cr.email
   return render(request,'profile.html',{'name':pfname,'contact':pcontact,'email':pemail})


def tutorial(request):
    return render(request,'tutorial.html')
 
 
# service views


def ser_home(request):
    return render(request,'ser_home.html')


def ser_register(request):
   if request.method =='POST':
      lino = request.POST.get('rlino')
      fname = request.POST.get('rfname')
      phone = request.POST.get('rcontact')
      email = request.POST.get('remail')
      location = request.POST.get('rlocation')
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      service_reg(license_no=lino,fullname=fname,contact=phone,email=email,location=location,username=uname,password=passw).save()
      return render(request,'ser_login.html')
   else:
      return render(request,'ser_register.html')


def ser_login(request):
   if request.method=='POST':
      lino =  request.POST.get('rlino')
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      cr = service_reg.objects.filter(license_no=lino,username=uname,password=passw)
      if cr:
         details = service_reg.objects.get(username=uname, password = passw,license_no=lino)
         username = details.username
         request.session['cs']=username
         lino = details.license_no
         request.session['lcu']=lino
         
         return render(request,'ser_home.html')
      else:
         message="Invalid Username Or Password"
         return render(request,'ser_login.html',{'me':message})
   else: 
      return render(request,'ser_login.html')


def ser_profile(request):
   c=request.session['lcu']
   cr=service_reg.objects.get(license_no=c)
   plino=cr.license_no
   pfname=cr.fullname
   pcontact=cr.contact
   pemail=cr.email
   plocation=cr.location
   return render(request,'ser_profile.html',{'lino':plino,'name':pfname,'contact':pcontact,'email':pemail,'location':plocation})
 

def feedback(request):
   fname=request.session['cs']
   if request.method =='POST':
      phone = request.POST.get('fphone')
      email = request.POST.get('fmail')
      msg = request.POST.get('fmsg')
      feed(fullname=fname,phone=phone,email=email,message=msg).save()
      return render(request,'home.html')
   else:
      return render(request,'feedback.html',{'fname':fname})
   
   
# stations view


def stations(request):
    data=station.objects.all()
    return render(request,'stations.html',{'data':data})
 
 
def add_station(request):
   lino=request.session['lcu']
   if request.method =='POST':
      fname = request.POST.get('rfname')
      time = request.POST.get('rtime')
      location = request.POST.get('rlocation')
      contact = request.POST.get('rcontact')
      speed = request.POST.get('rspeed')
      price = request.POST.get('rprice')
      status = request.POST.get('rstatus')
      station(license_no=lino,name=fname,time=time,location=location,contact=contact,speed=speed,price=price,status=status).save()
      return render(request,'ser_home.html')
   else:
      return render(request,'add_station.html',{'lino':lino})


# services view 


def services(request):
    data=service.objects.all()
    return render(request,'services.html',{'data':data})
 
 
def add_service(request):
   lino=request.session['lcu'] 
   if request.method =='POST':
      fname = request.POST.get('rfname')
      time = request.POST.get('rtime')
      location = request.POST.get('rlocation')
      price = request.POST.get('rprice')
      contact = request.POST.get('rcontact')
      status = request.POST.get('rstatus')
      service(license_no=lino,name=fname,time=time,location=location,price=price,contact=contact,status=status).save()
      return render(request,'ser_home.html')
   else:
      return render(request,'add_service.html',{'lino':lino})


# station  payment view


def payment(request,id):
 if request.method == 'POST':
    selected_time = request.POST.get('time')
    
    c = request.session['cs']
    sr = reg.objects.get(username=c)
    cr = station.objects.get(id=id)
    lino = cr.license_no
    pname = cr.name
    ploc = cr.location
    price = cr.price
    pfname = sr.fullname
    pcon = sr.contact 
    pmail = sr.email
    totalprice = 0
    e = int(price)
    totalprice = int(e*100)
    pay(license_no=lino,fullname=pfname,contact=pcon,email=pmail,name=pname,time=selected_time,location=ploc,amount=price).save()
    print(totalprice)
    
         
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
    s.starttls()
 
# Authentication
    s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
 
# message to be sent
    number = random.randint(10000,1000000)
    msg = str(number)
    message = f"Your Slot Booked Successfully , Your Onetime Code Is {msg}"
# sending the mail
    s.sendmail("nefsal003@gmail.com", pmail, message)
 
# terminating the session
    s.quit()   
    
    
    
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    #amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment.html', context=context)


 
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_failed.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_failed.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


# service  payment view


def payments(request,id):
 
 
    c = request.session['cs']
    sr = reg.objects.get(username=c)
    cr = service.objects.get(id=id)
    lino = cr.license_no
    pname = cr.name
    ptime = cr.time
    ploc = cr.location
    price = cr.price
    pfname = sr.fullname
    pcon = sr.contact 
    pmail = sr.email
    totalprice = 0
    e = int(price)
    totalprice = int(e*100)
    pay(license_no=lino,fullname=pfname,contact=pcon,email=pmail,name=pname,time=ptime,location=ploc,amount=price).save()
    print(totalprice)
    
         
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
    s.starttls()
 
# Authentication
    s.login("nefsal003@gmail.com", "htxalvzrrkxupspv")
 
# message to be sent
    number = random.randint(10000,1000000)
    msg = str(number)
    message = f"Your Service Booked Successfully , Your Onetime Code Is {msg}"
# sending the mail
    s.sendmail("nefsal003@gmail.com", pmail, message)
 
# terminating the session
    s.quit()   
    
    
    
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    #amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payments.html', context=context)



# admin views

def admin_home(request):
    return render(request,'admin_home.html')

def admin_reg(request):
   if request.method =='POST':
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      super_user(username=uname,password=passw).save()
      return render(request,'admin_login.html')
   else:
      return render(request,'admin_reg.html')


def admin_login(request):
   if request.method=='POST':
      uname = request.POST.get('runame')
      passw = request.POST.get('rpass')
      print(uname)
      print(passw)
      cr = super_user.objects.filter(username=uname,password=passw)
      if cr:
         details = super_user.objects.get(username=uname, password = passw)
         username = details.username
         request.session['cs']=username

         return render(request,'admin_home.html')
      else:
         message="Invalid Username Or Password"
         return render(request,'admin_login.html',{'me':message})
   else: 
      return render(request,'admin_login.html')

# booking views

def bookings(request):
    c = request.session.get('cs')
    values = pay.objects.filter(fullname=c)
    return render(request, 'bookings.html', {'values': values})
 
# orders views

def orders(request):
   lcu = request.session.get('lcu')
   values = pay.objects.filter(license_no=lcu)
   return render(request, 'orders.html', {'values': values})





# users list view

def users_list(request):
    data=reg.objects.all()
    return render(request,'users_list.html',{'data':data})


def delete_record1(request,id):
    data=reg.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')



def stations_list(request):
    data=station.objects.all()
    return render(request,'stations_list.html',{'data':data})


def delete_record2(request,id):
    data=station.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')


def services_list(request):
    data=service.objects.all()
    return render(request,'services_list.html',{'data':data})


def delete_record3(request,id):
    data=service.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')

def feedback_list(request):
    data=feed.objects.all()
    return render(request,'feedback_list.html',{'data':data})


def delete_record4(request,id):
    data=feed.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')

def payment_list(request):
    data=pay.objects.all()
    return render(request,'payments_list.html',{'data':data})


def delete_record5(request,id):
    data=pay.objects.get(id=id)
    data.delete()
    return render(request,'admin_home.html')


def view_stations(request):
    license_no = request.session.get('lcu')
    stations = station.objects.filter(license_no=license_no)
    return render(request, 'view_station.html', {'stations': stations})

def delete_station(request,id):
    data=station.objects.get(id=id)
    data.delete()
    return render(request,'ser_home.html')

def view_services(request):
    license_no = request.session.get('lcu')
    services = service.objects.filter(license_no=license_no)
    return render(request, 'view_service.html', {'services': services})

def delete_service(request,id):
    data=service.objects.get(id=id)
    data.delete()
    return render(request,'ser_home.html')


def reviews(request):
   lcu = request.session.get('lcu')
   values = feed.objects.filter(phone=lcu)
   return render(request, 'reviews.html', {'data': values})


def stations_search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        data= station.objects.filter(location=search)
        return render(request,'stations.html',{'data':data})

   
def services_search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        data= service.objects.filter(location=search)
        return render(request,'services.html',{'data':data})
    
def update_status(request):
    if request.method == 'POST':
        lino = request.POST.get('lino')
        print(lino)
        status = request.POST.get('status')
        dt=station.objects.get(license_no=lino)
        dt.status = status
        dt.save()
        return redirect('view_stations') 
    
def update_service(request):
    if request.method == 'POST':
        lino = request.POST.get('lino')
        print(lino)
        status = request.POST.get('status')
        dt=service.objects.get(license_no=lino)
        dt.status = status
        dt.save()
        return redirect('view_services') 