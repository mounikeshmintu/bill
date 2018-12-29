from django.contrib import admin
from .models import Product,Category,Direct
from django.urls import reverse
from django.utils.html import format_html


# Register your models here
# def order_pdf(obj):
#  return "<a href='{}'>pdf</a>".format(
#  reverse('orders:admin_order_pdf', args=[obj.id]))
# order_pdf.allow_tags = True
# order_pdf.short_description = 'PDF bill'
class DirectAdmin(admin.ModelAdmin):
    def order_pdf(obj):
        url=reverse('orders:admin_order_pdf', args=[obj.id])
        return format_html("<a href='{}'>{}</a>", url, "pdf")
    order_pdf.allow_tags = True
    order_pdf.short_description = 'PDF bill'
    list_display=['id','name','grand_total','phone_number',order_pdf,'date']
# class DirectAdmin(admin.ModelAdmin):
#     def order_pdf(obj):
#      # return "<a href='{}'>pdf</a>".format(
#      url=reverse('orders:admin_order_pdf', args=[obj.id])
#      return "http://localhost:8000" + url
#     order_pdf.allow_tags = True
#     order_pdf.short_description = 'PDF bill'
#     list_display=['id','name','price','phone_number',order_pdf]
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Direct,DirectAdmin)


# class OrderAdmin(admin.ModelAdmin):
#     list_display = [
#     order_pdf]
#
