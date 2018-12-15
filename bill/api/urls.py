"""billing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from .serializers import ProductSerializer
from .views import ProductView,DirectView,Direct,admin_order_pdf,create_pdf
# from .views import ProducList

app_name = 'orders'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('direct/',DirectView.as_view(),name='direct'),
    # path('bill/',Direct.as_view(),name='direct'),

    re_path(r'^bill/(?P<order_id>\d+)/pdf/$',
        admin_order_pdf,
     name='admin_order_pdf'),
    # re_path(r'^product/(?P<id>\d+)/$', ProductView),
    re_path(r'^product/(?P<id>\d+)/$',ProductView),
    path('test',create_pdf)



    # path('product(?P<id>\d+)',ProductView,name='product'),

    # path('product', ProductSerializer),
    # path('product', ProducList.as_view()),

]
