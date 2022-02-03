from django.db import models
from django.contrib.auth.models import User

from Yuvak.models import YuvakProfile
    
class KaryakarProfile(models.Model):
    profile = models.OneToOneField(YuvakProfile,on_delete=models.CASCADE,null=True,blank=True,related_name="ProfileInfo")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,)
    Yuvaks = models.ManyToManyField(YuvakProfile,null=True, blank=True,)

    def __str__(self):
        return self.profile.FirstName + " " + self.profile.MiddleName +" " + self.profile.SurName

