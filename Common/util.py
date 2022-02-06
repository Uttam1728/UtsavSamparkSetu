from datetime import date, datetime
from FolloWUp.models import FollowUp
from Mandal.models import Karyakram
from django.db.models import Q

def is_member(user, groupName):
    return user.groups.filter(name=groupName).exists()


def is_followUpDone(yuvak, samparkKarykar, event):
    return FollowUp.objects.filter(Karyakram=event, 
                                    SamparkKarykar__user=samparkKarykar, 
                                    Yuvak=yuvak).exists()

def getLatestKarykram(samparkKarykar):
    mandal = samparkKarykar.karyakarprofile.mandal
    curr_date = datetime.now()
    return Karyakram.objects.filter(Q(Mandal=mandal) & 
                                        (Q(Start_date__lte=curr_date) |
                                        Q(End_date__gte=curr_date)) ).order_by('Karyakram_date')
