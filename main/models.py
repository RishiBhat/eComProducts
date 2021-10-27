
from django.db import models
from django.db.models.base import Model

# Create your models here.




class Product(models.Model):
    prname=models.CharField(max_length=500)
    prtype=models.CharField(max_length=500)
    pr=models.CharField(max_length=500)
    prprice=models.IntegerField(default=400)
    #pr=models.IntegerField(default=400)
    produ=models.CharField(max_length=500, default="")
    prprice=models.IntegerField(default=400)
    prqty=models.IntegerField(default=80)
    prtotal=models.IntegerField(null=True, blank= True)
    primage = models.ImageField(upload_to='images/', default='',blank=True)
    
    
    def __str__(self):
        return self.prname
    
    def save(self, *args, **kwargs): 
        self.prtotal = self.prqty * self.prprice
        super(Product, self).save(*args, **kwargs)


   