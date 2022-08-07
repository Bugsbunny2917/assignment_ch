from abc import abstractclassmethod
import email
from inspect import classify_class_attrs
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    
    
    

    class Meta:
        abstract = True

class Todo(BaseModel):
    
    gender = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    # location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dob = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    cell = models.CharField(max_length=50)
    # id = models.CharField(primary_key=True, max_length=255)
    nat = models.CharField(max_length=100)
    age = models.CharField(max_length=5)


