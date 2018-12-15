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

# @api_view(['GET'])
# @renderer_classes((JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer))
# def meld_live_orders(request):
#     if request.method =='GET':
#         current_orders = Meld_Sales.objects.values_list('TicketNo',flat=True).distinct()
#         prev_orders = Meld_Order.objects.values_list('TicketNo',flat =True).distinct()
#
#         live_orders = live_order_generator(current_orders,prev_orders)
#
#         return render(request,'live_orders.html',{'live_orders':live_orders})
# @api_view(['GET'])
# @renderer_classes((JSONRenderer,TemplateHTMLRenderer))
def admin_order_pdf(request, order_id, *args, **kwargs):
# def admin_order_pdf(request, order_id):

    queryset=D.objects.all()
    # serializer=
    # order=D.objects.get(order_id)
    order = get_object_or_404(queryset, id=order_id)
    type=order.type
    price=order.price
    discount=order.discount
    total=price-discount
    # print()
    template=get_template('bill/b.html')
    data={
    'order': order,'total':total,'type':type
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
