from django.db import models
from django.contrib.auth.models import User
from Mandal.models import MandalProfile

from Yuvak.models import YuvakProfile
    
class KaryakarProfile(models.Model):
    profile = models.OneToOneField(YuvakProfile,on_delete=models.CASCADE,null=True,blank=True,related_name="ProfileInfo")
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True,)
    Yuvaks = models.ManyToManyField(YuvakProfile,blank=True,)
    mandal = models.ForeignKey(MandalProfile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.mandal.__str__() + ": " +self.profile.FirstName + " " + self.profile.MiddleName +" " + self.profile.SurName

