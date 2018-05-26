from django.db import models
from django.utils import timezone

from django.urls import reverse
# Create your models here.


class PurchaseDetail(models.Model):
    WOOD = 'Wood'
    GLASS = 'Glass'
    PLASTIC = 'Plastic'
    LEATHER = 'Leather'
    FABRIC = 'Fabric'
    STEEL = 'Steel'
    PRODUCT_CHOICES = (
        (WOOD, 'Wood'),
        (GLASS, 'Glass'),
        (PLASTIC, 'Plastic'),
        (LEATHER, 'Leather'),
        (FABRIC,'Fabric'),
        (STEEL, 'Steel'),
    )
    product_name =  models.CharField(max_length=30,
                                    choices=PRODUCT_CHOICES,
                                    default=WOOD,)
    quantity = models.PositiveSmallIntegerField(blank=False)
    rate =  models.IntegerField(blank=False)
    total = models.IntegerField(blank=False)
    remarks = models.CharField(max_length=250)
    def __str__(self):
        return (self.product_name)
    
    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
    
class Purchase(models.Model):
    invoice = models.SmallIntegerField(blank=False,primary_key=True)
    ch_no = models.SmallIntegerField(blank=True)
    vendor = models.CharField(max_length=128, blank=False)
    date = models.DateTimeField(default=timezone.now, blank=False)
    description = models.TextField(max_length=4096, blank=True, null=True)
    purchase_detail =models.ManyToManyField(PurchaseDetail)


    def __str__(self):
        return self.vendor

    def get_absolute_url(self):
        return reverse('entry:purchase_detail', kwargs={'pk': self.pk})

