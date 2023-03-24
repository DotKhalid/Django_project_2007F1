from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Subject = models.CharField(max_length=30)
    Message = models.TextField()


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30)
    Price = models.IntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,default=1)
    Description = models.TextField()
    image = models.ImageField( upload_to='static/themes/images/products/', height_field=None, width_field=None, max_length=None)

    # @staticmethod
    # def get_all_Products():
    #     return Product.objects.all()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

# Create your models here.
