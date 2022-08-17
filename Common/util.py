from datetime import datetime
from io import StringIO

import pandas as pd
from django.db.models import Q, Count
from django.forms.models import model_to_dict

from FolloWUp.models import FollowUp, FollowupStatus
from Mandal.models import Karyakram
from Yuvak.models import SatsangProfile


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
                                     Q(End_date__gte=curr_date))).order_by('Karyakram_date')


def messageIcons(phoneNo, size=27, message=True):
    buttons = ''
    buttons += "&nbsp; <a href='https://wa.me/+91{}' target='_blank'><i class='fa fa-whatsapp' style='font-size:{}px;color:green'></i></a>".format(
        phoneNo, size)
    buttons += "&nbsp; <a href='tel:+91{}' target='_blank'> <i class='fa fa-volume-control-phone' style='font-size:{}px;color:deepskyblue;margin-left:5px'></i> </a>".format(
        phoneNo, size)
    if message:
        buttons += "&nbsp; <a href='sms:+91{}' target='_blank'> <i class='fa fa-commenting-o' style='font-size:{}px;color:lightblue;margin-left:5px'></i> </a>".format(
            phoneNo, size)
        # buttons += "&nbsp; <a href='sms:+91{}'> <i class='fa fa-send-o' style='font-size:27px;color:deepskyblue;margin-left:5px'></i> </a>".format(phoneNo)

    # <img src='/Photos/whatsapp-logo.png' alt='Whatsapp' width='25'📲 height='25'>

    return buttons


def Profile_Completion(obj):
    fields_names = [f.name for f in obj._meta.fields]
    completed = 0
    for field_name in fields_names:
        value = getattr(obj, field_name)
        completed += not (value is None or value == '')
    ratio = (completed / len(fields_names)) * 100

    return int(ratio)


def getMandal(user):
    return user.yuvakprofile.mandal


def create_Excel_queryset(queryset):
    records = []
    if queryset.exists():
        for yuvak in queryset:
            if queryset.model is FollowUp:
                yuvak = yuvak.Yuvak
            elif queryset.model is SatsangProfile:
                yuvak = yuvak.yuvakProfile
            meta_fileds = model_to_dict(yuvak)
            if yuvak.ProfilePhoto:
                meta_fileds["ProfilePhoto"] = yuvak.ProfilePhoto.url
            del meta_fileds["mandal"]
            records.append(meta_fileds)

    df = pd.DataFrame(records)
    df.index += 1
    s = StringIO()
    df.to_csv(s, encoding='utf-8', index=True, )
    return s


def create_Excel_karyakar_vrund_queryset(queryset):
    records = []
    if queryset.exists():
        for vrund in queryset:
            for yuvak in vrund.yuvaks:
                meta_fileds = model_to_dict(yuvak)
                if yuvak.ProfilePhoto:
                    meta_fileds["ProfilePhoto"] = yuvak.ProfilePhoto.url
                del meta_fileds["mandal"]
                records.append(meta_fileds)

    df = pd.DataFrame(records)
    df.index += 1
    s = StringIO()
    df.to_csv(s, encoding='utf-8', index=True, )
    return s


def make_report(karyakram_id):
    records = list((FollowUp.objects.filter(Karyakram=karyakram_id, Status=FollowupStatus.Pending)
                    .values_list('KaryKarVrund__karykar1profile__FirstName', 'KaryKarVrund__karykar2profile__FirstName')
                    .annotate(yuvaks=Count('Status'))
                    .order_by()
                    ))
    df = pd.DataFrame(records)
    csvstream = StringIO()
    df.to_csv(csvstream, encoding='utf-8', index=False, )
    return csvstream
