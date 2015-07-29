from django.contrib import admin
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
        'my_field',
        'total',
    )

admin.site.register(Category)
admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)
