from django.db import models
choice=(('Not Available','Not Available'),('Available','Available'))

# Create your models here.
class reg(models.Model):
    fullname=models.CharField(max_length=20)
    contact=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class service_reg(models.Model):
    license_no=models.IntegerField()
    fullname=models.CharField(max_length=20)
    contact=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
class feed(models.Model):
    fullname=models.CharField(max_length=20)
    phone=models.IntegerField()
    message=models.CharField(max_length=20)
    email=models.EmailField()
    
class station(models.Model):
    license_no=models.IntegerField()
    name=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    contact=models.IntegerField()
    speed=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    status=models.CharField(max_length=20,choices=choice)
    
class service(models.Model):
    license_no=models.IntegerField()
    name=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    contact=models.IntegerField()
    status=models.CharField(max_length=20,choices=choice)
    
class pay(models.Model):
    license_no=models.IntegerField()
    fullname=models.CharField(max_length=20)
    contact=models.IntegerField()
    email=models.EmailField()
    name=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    amount=models.IntegerField()
    
class super_user(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    

    