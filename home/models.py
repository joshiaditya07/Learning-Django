from django.db import models

# Create your models here.
# model means table in database: basically we are creating a table in database with the help of models.py file. we can create as many tables as we want in database by creating models in models.py file. each model will represent a table in database. each attribute of model will represent a column
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField( null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    file = models.FileField()
    

class Product(models.Model):
    pass


