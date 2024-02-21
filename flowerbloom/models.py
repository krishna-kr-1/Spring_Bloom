
#flowerbloom/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    mobile=models.CharField(max_length=12,verbose_name='Phone Number')
    address=models.TextField(verbose_name='Address')

    def __str__(self):
        return self.first_name+" "+self.last_name
class Flowershop(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=255, verbose_name='Flower Name')
    admin_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Flower Price')

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=50,verbose_name='Category name')
    def __str__(self):
        return self.cat_name
class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150,verbose_name='product name')
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category name')
    delivery_info = models.TextField()
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Delivery Charge')
    product_info=models.TextField()


    def __str__(self):
        return self.name
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
class WishlistItem(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=255)
    payment_id=models.CharField(max_length=255)
    address=models.TextField()

