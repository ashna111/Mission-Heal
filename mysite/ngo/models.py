from django.db import models
from django.urls import reverse

# Create your models here.
class Ngo(models.Model):
    ngo_name=models.CharField(max_length=250)
    ngo_logo=models.CharField(max_length=1000)
    ngo_loc=models.CharField(max_length=250)
    ngo_relieftype=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('ngo:index')

    def __str__(self):
        return self.ngo_name +' - '+self.ngo_loc+'--'+self.ngo_relieftype


class Ngodetails(models.Model):
    ngo=models.ForeignKey(Ngo,on_delete=models.CASCADE)
    ngo_details=models.CharField(max_length=3000)
    ngo_address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.ngo_details +' - '+self.ngo_address