from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title


class Dish(models.Model):
    class Meta:
        verbose_name_plural = "Dishes"

    name = models.TextField(max_length=200)
    category = models.ForeignKey(Category)
    description = models.TextField(max_length=200, blank=True)
    weight = models.FloatField(max_length=6)
    price = models.FloatField(max_length=6)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"

    items = models.ManyToManyField(Dish, through='Calculate')
    date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default=1)

    def total(self):
        b=0
        for item in Calculate.objects.filter(order=self):
            a = item.dish.price*item.count
            b+=a
        return b


    def my_field(self):
        a = ''
        for item in Calculate.objects.filter(order=self):
            a += ", " + item.dish.name + 'x' + str(item.count)
        return a[1:]


    my_field.short_description = 'Column description'


class Calendar(models.Model):
    date = models.DateField()
    dish = models.ForeignKey(Dish)

    def __str__(self):
        return str(self.date)


class Calculate(models.Model):
    order = models.ForeignKey(Order)
    dish = models.ForeignKey(Dish)
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.order.date)
