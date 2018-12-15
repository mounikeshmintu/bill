from  rest_framework import serializers
from bill.models import Product,Direct
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields=('name','total','category','rate')
class DirectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Direct
        fields=('name','price','discount','phone_number','id')
