from django.db import models

# Create your models here.
class Crud(models.Model):
    name=models.CharField(max_length=100,blank=True)
    age=models.IntegerField(blank=True)
    TOTAL_FORMS=models.IntegerField(blank=True,null=True)
    INITIAL_FORMS=models.IntegerField(blank=True,null=True)