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
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    rate=models.IntegerField()
    # peices=models.IntegerField(default=True)
    # total=models.PositiveIntegerField(editable=False)
    # def save(self, *args, **kwargs):
    #     total = self.rate * self.peices
    #     super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Direct(models.Model):
    type=models.CharField(max_length=128,null=True,blank=True)
    name=models.CharField(max_length=128)
    # created=models.DateTimeField(auto_now_add=True,blank=True)
    # date = models.DateTimeField(default=timezone.now(), blank=True,null=True)

    price=models.IntegerField()
    discount=models.IntegerField()
    phone_number=models.BigIntegerField(null=True)
    def __str__(self):
        return self.name
