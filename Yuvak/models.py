from django.db import models
from django.contrib.auth.models import User

from Mandal.models import MandalProfile
    
class YuvakProfile(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    WhatsappNo = models.CharField(max_length=10, db_index=True)
    HomePhoneNo = models.CharField(max_length=10, null=True, blank=True)
    AddressLine1 = models.CharField(max_length=1000)
    AddressLine2 = models.CharField(max_length=1000,null=True, blank=True,)
    PinCode = models.CharField(max_length=6, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,)
    mandal = models.ForeignKey(MandalProfile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.FirstName + " " + self.MiddleName + " " + self.SurName

