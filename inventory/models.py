from django.db import models

# Create your models here.
class Item(models.Model):
    item_name =     models.CharField(max_length = 64)

    def __str__(self):
        return self.item_name

class ItemDetail(models.Model):
    inventory =     models.ForeignKey(Item,on_delete = models.CASCADE)
    item_quantity = models.PositiveIntegerField(default = 0)
    item_rate =     models.IntegerField(default = 0)
    item_status =   models.BooleanField(default = True)

    def __str__(self):
        return self.inventory.item_name
