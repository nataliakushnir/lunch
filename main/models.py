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

