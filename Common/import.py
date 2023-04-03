# --- Description --- #
# Sets the reporter ID by looking at the author field
# BEWARE : if the names are common - which has a high probability then this method will overwrite people's submissions

# --- Usage Instructions --- #
# python3 manage.py shell
# >> exec(open('./Common/import.py').read())

import csv

from Mandal.models import MandalProfile
# get the correct versions of models using the app registry
from Yuvak.models import YuvakProfile

yuvakmandal = MandalProfile.objects.filter(Name="Utsav").first()
print(yuvakmandal)
if yuvakmandal:
    with open('all yuvak.csv') as csv_file:
        reader = csv.reader(csv_file)
        # header = next(reader)
        i = 0
        for row in reader:
            print(row)
            if not YuvakProfile.objects.filter(WhatsappNo=row[3]).exists():
                yuvak = YuvakProfile(FirstName=row[0], MiddleName=row[1], SurName=row[2], WhatsappNo=row[3],
                                     Soc_Name=row[4],
                                     mandal_id=yuvakmandal.pk)
                yuvak.save()
                i += 1
                print(i)
                print('yuvak', yuvak)
