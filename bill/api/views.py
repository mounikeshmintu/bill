from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .serializers import ProductSerializer,DirectSerializer
from rest_framework import mixins
from bill.models import Product,Direct
from rest_framework import serializers
from rest_framework.decorators import api_view,renderer_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
import json
from django.views.generic import View
from .serializers import ProductSerializer,DirectSerializer
from bill.models import Direct as D
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
# import weasyprint
from django.template.loader import get_template
from bill.utils import render_to_pdf
from rest_framework.renderers import JSONRenderer
import pdfkit
from django.http import HttpResponse
from django.template import loader
import pdfkit
# config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

@api_view(['GET','POST'])
def ProductView(request,id):
    stat = get_object_or_404(Product,id=id)
    serializer =ProductSerializer

    nice=stat.total
    return Response(json.dumps(nice))
        # serializer = ProductSerializer(stat)
        # return Response(serializer.data)
        # status = get_object_or_404(id=request.POST.get('id', ''))
            # serializer = serializers.statusSerializer(stat,many=True)
    # nice = str(stat.total)
    # print(nice)
    # return Response(json.loads(reader(nice))

class DirectView(mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class=DirectSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class Direct(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bill/bill.html'

    def get(self, request):
        queryset = D.objects.all()
        return Response({'direct': queryset})
def admin_order_pdf(request, order_id, *args, **kwargs):
    queryset=D.objects.all()
    order = get_object_or_404(queryset, id=order_id)
    type=order.type
    price=order.price
    meters =order.meters
    price_total=price*meters
    discount=order.discount
    total=price
    grand_total=total-discount
    type2=order.type2

    if type2 == None:
        price2=None
        meters2=None
        # discount2=None
        total2=None
    else:
        price2=order.price2
        meters2=order.meters2
        price2_total=price2*meters2
        discount=order.discount

        # total2=price2-discount2
        total2=price_total+price2_total
        grand_total=total2-discount

    type3=order.type3
    if type3 == None:
        price3=None
        meters3=None
        discount=None
        total3=None
    else:
        price3=order.price3
        meters3=order.meters3
        price3_total=price3*meters3
        discount=order.discount
        # total3=price3-discount3
        total3=price_total+price2_total+price3_total
        grand_total=total3-discount

    type4=order.type4
    if type4 == None:
        price4=None
        meters4=None
        # discount4=None
        total4=None
    else:
        price4=order.price4
        meters4=order.meters4
        price4_total=price4*meters4
        discount=order.discount
        total4=price_total+price2_total+price3_total+price4_total
        grand_total=total4-discount
    type5=order.type5
    if type5 == None:
        price5=None
        meters5=None
        discount=None
        total5=None
    else:
        price5=order.price5
        meters5=order.meters5
        price5_total=price5*meters5
        discount=order.discount
        total5=price_total+price2_total+price3_total+price4_total+price5_total
        grand_total=total5-discount
    # else:
    #     price2=None
    # if price2 !=  None:

        # total2=price2-discount2
        # return total2
    # else:
        # total2=None
        # return price2,meters2,price2,total2
    # else:
    #     price2=None
    #     meters2=None
    #     discount2 =None
    # print()
    template=get_template('bill/b.html')
    data={

    'order': order,
    'total':total,
    'type':type,
    'price':price,
    'price_total':price_total,
    'meters':meters,
    'discount':discount,
    'type2':type2,
    'price2':price2,
    'price2_total':price2_total,

    # 'discount2':discount2,
    'total2':total2,
    'meters2':meters2,
    'type3':type3,
    'price3':price3,
    'price3_total':price3_total,
    # 'discount3':discount3,
    'total3':total3,
    'meters3':meters3,
    'type4':type4,
    'price4':price4,
    'price4_total':price4_total,
    # 'discount4':discount4,
    'total4':total4,
    'meters4':meters4,
    'type5':type5,
    'price5':price5,
    'price5_total':price5_total,
    # 'discount5':discount5,
    'total5':total5,
    'meters5':meters5,
    'grand_total':grand_total,

        }
    html = render_to_pdf('bill/b.html',data)
    return HttpResponse(html, content_type='application/pdf')

    # response = HttpResponse(html,content_type='application/pdf')
    # response['Content-Disposition'] = 'filename=\
    # "order_{}.pdf"'.format(order.id)
    # weasyprint.HTML(string=html).write_pdf(response,
    # stylesheets=[weasyprint.CSS(
    # settings.STATIC_ROOT + 'css/pdf.css')])
    # return response

def create_pdf(request):
    html = loader.render_to_string('bill/b.html', {})
    # pdfkit.from_string('Hello!', 'out.pdf',configuration = config)

    output= pdfkit.from_string(html, output_path=False,configuration=pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe"))
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response
