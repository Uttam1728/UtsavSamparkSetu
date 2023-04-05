# --- Description --- #
# Sets the reporter ID by looking at the author field
# BEWARE : if the names are common - which has a high probability then this method will overwrite people's submissions
import csv

from Mandal.models import MandalProfile
from SamparkKarykar.constant import Alphabet
from SamparkKarykar.models import KaryakarProfile
from Yuvak.models import YuvakProfile

# --- Usage Instructions --- #
# python3 manage.py shell
# >> exec(open('./Common/makeVrund.py').read())

# get the correct versions of models using the app registry

yuvakmandal = MandalProfile.objects.filter(Name="Utsav").first()
print(yuvakmandal)
karykar = []
yuvaks = []
if yuvakmandal:
    with open('all yuvak.csv') as csv_file:
        reader = csv.reader(csv_file)
        # header = next(reader)
        i = 0
        for row in reader:
            print(row)

            yuvak = YuvakProfile.objects.filter(WhatsappNo=row[4])
            if yuvak.exists():
                yuvak.delete()

            yuvak = YuvakProfile(FirstName=row[1], MiddleName=row[2], SurName=row[3], WhatsappNo=row[4],
                                 HomePhoneNo=row[5], Email=row[6], Soc_Name=row[7],
                                 mandal_id=yuvakmandal.pk)
            yuvak.save()
            if i <= 1:
                karykar.append(yuvak)
            else:
                yuvaks.append(yuvak)
            i += 1
            print(i)
            # print(karykar)
            # print(yuvaks)
            # print('yuvak', yuvak)
        karykarvrund = KaryakarProfile()
        karykarvrund.karykar1profile_id = karykar[0].pk
        karykarvrund.karykar2profile_id = karykar[1].pk
        karykarvrund.mandal_id = yuvakmandal.pk
        karykarvrund.group_number = Alphabet.D
        karykarvrund.save()
        karykarvrund.Yuvaks.add(*yuvaks)
