from django.contrib import admin

from .models import Product
#admin.site.register(login)


admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'prname','prtype', 'pr','prprice', 'prqty', 'prtotal','primage']

