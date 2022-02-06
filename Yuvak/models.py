from django.db import models
from django.contrib.auth.models import User

from Mandal.models import MandalProfile
    
class YuvakProfile(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    WhatsappNo = models.CharField(max_length=10, db_index=True)
    HomePhoneNo = models.CharField(max_length=10, null=True, blank=True)
    HouseNo = models.IntegerField(verbose_name="House/Flat No.")
    Soc_Name = models.CharField(max_length=50,verbose_name="Sociaty/Apartment Name")
    LandMark = models.CharField(max_length=100)
    Area = models.CharField(max_length=50)
    PinCode = models.CharField(max_length=6, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,)
    mandal = models.ForeignKey(MandalProfile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.mandal.__str__() + ": "+ self.FirstName + " " + self.MiddleName + " " + self.SurName

