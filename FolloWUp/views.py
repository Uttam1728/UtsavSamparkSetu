from datetime import datetime

from django.http import HttpResponseRedirect

from FolloWUp.models import FollowUp


def myview(request):
    ...


# Create your views here.
def mark_attandance(request):
    if request.user.is_superuser:
        followup_id = request.GET.get('followup', 0)
        attandance = request.GET.get('present', False) == "True"
        FollowUp.objects.filter(pk=followup_id).update(Present=attandance, Attandance_Time=datetime.now())
        parent = request.GET.get('parent', 'admin')
        return HttpResponseRedirect(parent)
    return HttpResponseRedirect('admin')


def qr_scan(request):
    # # initalize the cam
    # cap = cv2.VideoCapture(0)
    # # initialize the cv2 QRCode detector
    # detector = cv2.QRCodeDetector()
    # while True:
    #     _, img = cap.read()
    #     # detect and decode
    #     data, bbox, _ = detector.detectAndDecode(img)
    #     # check if there is a QRCode in the image
    #     if data:
    #         a=data
    #         break
    #     # display the result
    #     cv2.imshow("QRCODEscanner", img)    
    #     if cv2.waitKey(1) == ord("q"):
    #         break

    # b=webbrowser.open(str(a))
    # cap.release()
    # cv2.destroyAllWindows()

    return HttpResponseRedirect('admin')
