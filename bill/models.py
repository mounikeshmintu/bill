from django.db import models
import datetime
from datetime import datetime
from django.utils import timezone


# Create your models here.
# class Piece(models.Model):
#    total=models.IntegerField(default=True)
#    # st=str(total)
#    product =models.ForeignKey('Product', on_delete=models.CASCADE, related_name='piecies')
#    def __str__(self):
#        return self.str(total)

class Product(models.Model):
    name=models.CharField(max_length=128)
    total=models.IntegerField(default=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,default=True)
    rate=models.IntegerField()


    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Direct(models.Model):
    type=models.CharField(max_length=128,null=True,blank=True)
    name=models.CharField(max_length=128)
    price=models.IntegerField()
    meters=models.FloatField(null=True,blank=True)

    # meters=models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2)
    discount=models.IntegerField(null=True)
    phone_number=models.BigIntegerField(null=True)
    type2=models.CharField(max_length=128,null=True,blank=True)
    meters2=models.FloatField(null=True,blank=True)
        # meters2=models.DecimalField(null=True,blank=True,max_digits=5, decimal_places=2)

    price2=models.IntegerField(null=True,blank=True)
    discount2=models.IntegerField(null=True,blank=True)
    # phone_number2=models.BigIntegerField(null=True)
    def __str__(self):
        return self.name
