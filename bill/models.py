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
    # date = models.DateTimeField(auto_now_add=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    name=models.CharField(max_length=128)
    phone_number=models.BigIntegerField(null=True)
    type=models.CharField(max_length=128,null=True,blank=True)
    price=models.IntegerField(null=True)
    meters=models.FloatField(null=True,blank=True)
    discount=models.IntegerField(null=True)
    type2=models.CharField(max_length=128,null=True,blank=True)
    meters2=models.FloatField(null=True,blank=True)
    price2=models.IntegerField(null=True,blank=True)
    # discount2=models.IntegerField(null=True,blank=True)
    type3=models.CharField(max_length=128,null=True,blank=True)
    meters3=models.FloatField(null=True,blank=True)
    price3=models.IntegerField(null=True,blank=True)
    # discount3=models.IntegerField(null=True,blank=True)
    type4=models.CharField(max_length=128,null=True,blank=True)
    meters4=models.FloatField(null=True,blank=True)
    price4=models.IntegerField(null=True,blank=True)
    # discount4=models.IntegerField(null=True,blank=True)
    type5=models.CharField(max_length=128,null=True,blank=True)
    meters5=models.FloatField(null=True,blank=True)
    price5=models.IntegerField(null=True,blank=True)
    grand_total=models.IntegerField(null=True,blank=True)
    # discount5=models.IntegerField(null=True,blank=True)
    # phone_number2=models.BigIntegerField(null=True)
    def __str__(self):
        return self.name
