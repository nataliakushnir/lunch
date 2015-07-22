from django.contrib import admin
<<<<<<< HEAD
from main.models import Order, Dish, Category


class DishAdmin(admin.ModelAdmin):
    model = Dish
    list_display = (
        'name',
        'category',
        'price',
    )


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = (
        'user',
        'date',
        'my_url_field'
    )


admin.site.register(Category)
admin.site.register(Dish, DishAdmin)
=======
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
>>>>>>> da983a13e6069f377d4068c3be960c08e95239dd
admin.site.register(Order, OrderAdmin)
