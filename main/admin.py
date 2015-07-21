from django.contrib import admin
from .models import Items, Orders, Order
# Register your models here.


class ItemsAdmin(admin.ModelAdmin):
    model = Items
    list_display = ('item_name', 'item_description', 'item_composition', 'item_weight', 'item_price', 'item_status', 'item_date_add')

class OrdersAdmin(admin.ModelAdmin):
    model = Orders
    list_display = ('order_date_published', 'order_date_target', 'order_status')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('Orders.order_items', )

admin.site.register(Items, ItemsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Order, OrderAdmin)
