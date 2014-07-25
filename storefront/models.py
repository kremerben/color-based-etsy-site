from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=120)
    shop_id = models.IntegerField()
    title = models.CharField(max_length=120)
    announcement = models.TextField()
    url = models.URLField()
    image = models.URLField()

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=120)
    category_id = models.IntegerField()
    description = models.TextField()
    price = models.CharField(max_length=20)
    url = models.URLField()
    style = models.CharField(max_length=120)
    shop = models.ForeignKey(Shop, related_name='shop')
    image = models.URLField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.name



