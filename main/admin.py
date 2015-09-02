from django.contrib import admin
from main.models import Order, Dish, Category, Calendar, Calculate


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
        'date',
        'my_field',
        'total',
    )


class CalculateAdmin(admin.ModelAdmin):
    model = Calculate
    list_display = (
        'order',
        'dish',
        'count',
    )


admin.site.register(Category)
admin.site.register(Calendar)
admin.site.register(Calculate)
admin.site.register(Dish, DishAdmin)
admin.site.register(Order, OrderAdmin)