# exec(open('./make_report.py').read())
import pandas as pd

from Mandal.models import MandalProfile


def make_report():
    karyakram_id = 9
    import pandas as pd
    from django.db.models import Count

    from FolloWUp.models import FollowUp, FollowupStatus

    records = list((FollowUp.objects.filter(Karyakram=karyakram_id, Status=FollowupStatus.Pending)
                    .values_list('KaryKarVrund__karykar1profile__FirstName', 'KaryKarVrund__karykar2profile__FirstName')
                    .annotate(dcount=Count('Status'))
                    .order_by()
                    ))
    df = pd.DataFrame(records)
    df.to_csv("testcsvfile.csv")


# def create_excel(modeladmin, request, queryset):
mandal = MandalProfile.objects.get(pk=1)
records = []
for karyakar_vrund in mandal.karyakarprofile_set.all():
    for yuvak in karyakar_vrund.Yuvaks.all():
        temp = dict()
        temp["karykar1"] = karyakar_vrund.karykar1profile.__str__()
        temp["karykar2"] = karyakar_vrund.karykar2profile.__str__()
        temp["yuvak"] = yuvak.__str__()
        records.append(temp)
df = pd.DataFrame(records)
df.index += 1
df.to_csv("karykar_yuvak.csv")
