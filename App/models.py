from django.db import models

# Create your models here.
class Signup(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    confirmpassword=models.CharField( max_length=50)
    
class Login(models.Model):
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    
class Products(models.Model):
    image=models.ImageField( upload_to='pics/')
    title=models.CharField( max_length=50)
    descript=models.CharField( max_length=50)
    price=models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    queries=models.TextField()
    
class Admins(models.Model):
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    
class AdminLogin(models.Model):
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    
class OrderNow(models.Model):
    fullname = models.CharField( max_length=50)
    fooditem = models.CharField( max_length=50)
    quantity = models.IntegerField()
    address = models.TextField()
    price = models.IntegerField()
    
    