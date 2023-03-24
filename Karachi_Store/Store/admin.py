from django.contrib import admin

from Store.models import Product
from Store.models import Category
from Store.models import Customer
from Store.models import Contact

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','Price','category','Description']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class CustomerDetails(admin.ModelAdmin):
    list_display = ['first_name','last_name']

class ContactDetails(admin.ModelAdmin):
    list_display = ['name','email','Subject','Message']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,CustomerDetails)
admin.site.register(Contact,ContactDetails)