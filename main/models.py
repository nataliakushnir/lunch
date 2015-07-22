<<<<<<< HEAD
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

    def my_url_field(self):
        a = ''
        for b in self.items.all():
            a += ", " + b.name
        return a[1:]

    my_url_field.short_description = 'Column description'
=======
from django.db import models
from django.db.models.fields.related import ManyToManyRel
import datetime
from django.utils import timezone

# Create your models here.

class Dishes(models.Model):
    class Meta():
        db_table = 'Dishes'

    def __str__(self):
        return self.dish_description
    dish_description = models.TextField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.dish_description

class Items(models.Model,):
    def __str__(self):
        return self.item_name

    def __unicode__(self):
        return u"%s" % self.item_composition

    def __unicode__(self):
        return u"%s" % self.item_name

    item_name = models.TextField(max_length=200)
    item_description = models.ForeignKey(Dishes)
    item_composition = models.TextField(max_length=200, blank=True)
    item_weight = models.CommaSeparatedIntegerField(max_length=20)
    item_price = models.FloatField(max_length=20)
    item_status = models.BooleanField(default=False)
    item_date_add = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    order_date_published = models.DateTimeField(auto_now_add=True)
    order_date_target = models.DateField()
    order_item = models.ManyToManyField(Items)
    order_status = models.BooleanField(default=True)

class Order(models.Model):
    order_items = models.ManyToManyField(Orders, related_name='order_items')

>>>>>>> da983a13e6069f377d4068c3be960c08e95239dd
