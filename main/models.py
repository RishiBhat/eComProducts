from django.db import models
from django.db.models.base import Model

# Create your models here.




class Product(models.Model):
    prname=models.CharField(max_length=500)
    prtype=models.CharField(max_length=500)
    pr=models.CharField(max_length=500)
    prprice=models.IntegerField(default=400)
    pr=models.IntegerField(default=400)
    prprice=models.IntegerField(default=400)
    prqty=models.IntegerField(default=80)
    prtotal=models.IntegerField(default=500)
    primage = models.ImageField(upload_to='upload_image', default='static/main/Dal.jpg')
    
    
    def upload_image(self, filename):
        return 'post/{static}/{main}'.format(self.title, filename)




    #model_pic= models.ImageField(upload_to=upload_image, default='blog/images/already.png')
    #created_date = models.DateTimeField(default = timezone.now)
    #published_date = models.DateTimeField(blank = True, null =True)


    #def upload_image(self, filename):
        #return 'post/{}/{}'.format(self.title, filename)