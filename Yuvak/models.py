from enum import IntEnum
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator
from Mandal.models import MandalProfile


class SSPStage(IntEnum) :
    No= 0
    prarambh = 1,
    pravesh = 2,
    parichay = 3,
    paravin = 4,
    Pragn_1 = 5,
    Pragn_2 = 6,
    Pragn_3 = 7
class YuvakProfile(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    WhatsappNo = models.CharField(max_length=10, db_index=True)
    HomePhoneNo = models.CharField(max_length=10, null=True, blank=True)
    HouseNo = models.IntegerField(verbose_name="House/Flat No.", null=True, blank=True)
    Soc_Name = models.CharField(max_length=50,verbose_name="Sociaty/Apartment Name", null=True, blank=True)
    LandMark = models.CharField(max_length=100, null=True, blank=True)
    Area = models.CharField(max_length=50, null=True, blank=True)
    PinCode = models.CharField(max_length=6, null=True, blank=True)
    Married = models.BooleanField(blank=True,null=True)
    DateOfBirth = models.DateField(blank=True,null=True)
    Education = models.CharField(max_length=100,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True,)
    mandal = models.ForeignKey(MandalProfile,on_delete=models.CASCADE)
    def __str__(self):
        return self.FirstName + " " + self.MiddleName + " " + self.SurName

class SatsangProfile(models.Model):
    yuvakProfile = models.OneToOneField(YuvakProfile,on_delete=models.CASCADE)
    NityaPuja = models.BooleanField(blank=True,null=True)
    NityaPujaYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    TilakChandlo = models.BooleanField(blank=True,null=True)
    TilakChandloYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    Satsangi = models.BooleanField(blank=True,null=True)
    SatsangiYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    AthvadikSabha = models.BooleanField(blank=True,null=True)
    AthvadikSabhaYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    Ravisabha = models.BooleanField(blank=True,null=True)
    RavisabhaYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    GharSatsang = models.BooleanField(blank=True,null=True)
    GharSatsangYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    SSP = models.BooleanField(blank=True,null=True)
    SSPStage = models.IntegerField( 
                default=SSPStage.No,
                choices=[(methods.value, methods.name) for methods in SSPStage]  # Choices is a list of Tuple
             )
    Ekadashi = models.BooleanField(blank=True,null=True)
    EkadashiYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    Niymit_Vanchan = models.BooleanField(blank=True,null=True)
    Niymit_VanchanYear = models.IntegerField(validators=[MaxValueValidator(30)],blank=True,null=True)
    


    def __str__(self):
        return self.yuvakProfile.__str__()


