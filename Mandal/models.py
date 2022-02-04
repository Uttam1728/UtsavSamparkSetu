from django.db import models

# from SamparkKarykar.models import KaryakarProfile
# from Yuvak.models import YuvakProfile

# Create your models here.

class MandalProfile(models.Model):
    Name = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name +" - "  + self.Area

class Karyakram(models.Model):
    Title = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=False)
    Start_date = models.DateTimeField(blank=True,null=True)
    End_date = models.DateTimeField(blank=True,null=True)
    Mandal = models.OneToOneField(MandalProfile,blank=True,null=True,on_delete=models.CASCADE)
    For_All = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Title


