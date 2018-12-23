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
    price=price*meters
    discount=order.discount
    total=price-discount
    type2=order.type2
    if type2 == None:
        # type2=None
        price2=None
        meters2=None
        discount2=None
        total2=None


        
    else:
        price2=order.price2
        meters2=order.meters2
    # if meters2 != None:
        price2=price2*meters2
        discount2=order.discount2
        total2=price2-discount2

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
    'meters':meters,
    'discount':discount,
    'type2':type2,
    'price2':price2,
    'discount2':discount2,
    'total2':total2,
    'meters2':meters2
        }
    html = render_to_pdf('bill/b.html',
    data)
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
