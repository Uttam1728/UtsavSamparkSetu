from django.db import models

from enum import IntEnum, IntEnum
from Mandal.models import Karyakram
from SamparkKarykar.models import KaryakarProfile
from Yuvak.models import YuvakProfile


class HowMethods(IntEnum) :
    Whatsapp = 1,
    Phonecall = 2,
    Telegram = 3,
    SMS = 4,
    InPerson = 5,
    Other = 6 

class FollowupStatus(IntEnum) :
    Pending = 1,
    Done = 2,
    No = 3,
    InProgress = 4


# Create your models here.
class FollowUp(models.Model):
    Karyakram = models.ForeignKey(Karyakram,on_delete=models.CASCADE)
    SamparkKarykar = models.ForeignKey(KaryakarProfile,on_delete=models.CASCADE)
    Yuvak = models.ForeignKey(YuvakProfile,on_delete=models.CASCADE)
    FollowUp_Time = models.DateTimeField(auto_now_add=True)
    LastFollowUp_Time = models.DateTimeField(auto_now=True)
    How = models.IntegerField(
                default=HowMethods.Other,
                choices=[(methods.value, methods.name) for methods in HowMethods]  # Choices is a list of Tuple
             )
    Remark = models.CharField(max_length=1000,blank=True,null=True)
    Status = models.IntegerField(
                default=FollowupStatus.Pending,
                choices=[(status.value, status.name) for status in FollowupStatus]  # Choices is a list of Tuple
             )

    def __str__(self):
        return self.Karyakram.__str__()