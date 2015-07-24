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

    items = models.ManyToManyField(Dish)
    user = models.ForeignKey(User)
    date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def total(self):
        sum = 0
        for i in self.items.all():
            sum += i.price
        return sum

    def my_field(self):
        a = ''
        for b in self.items.all():
            a += ", " + b.name
        return a[1:]

    my_field.short_description = 'Column description'
