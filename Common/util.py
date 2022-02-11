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


def messageIcons(phoneNo,size=27):
    buttons = ''
    buttons += "&nbsp; <a href='https://wa.me/+91{}' ><i class='fa fa-whatsapp' style='font-size:{}px;color:green'></i></a>".format(phoneNo,size)
    buttons += "&nbsp; <a href='tel:+91{}'> <i class='fa fa-volume-control-phone' style='font-size:{}px;color:deepskyblue;margin-left:5px'></i> </a>".format(phoneNo,size)
    buttons += "&nbsp; <a href='sms:+91{}'> <i class='fa fa-commenting-o' style='font-size:{}px;color:lightblue;margin-left:5px'></i> </a>".format(phoneNo,size)  
    # buttons += "&nbsp; <a href='sms:+91{}'> <i class='fa fa-send-o' style='font-size:27px;color:deepskyblue;margin-left:5px'></i> </a>".format(phoneNo)
    
    # <img src='/Photos/whatsapp-logo.png' alt='Whatsapp' width='25'📲 height='25'>

    return buttons

def Profile_Completion(obj):
        fields_names = [f.name for f in obj._meta.fields]
        completed = 0
        for field_name in fields_names:
            value = getattr(obj, field_name)
            completed += not(value is None or value == '')
        ratio = (completed / len(fields_names)) * 100
        
        return  ratio
        

def getMandal(user):
    return user.yuvakprofile.mandal
        