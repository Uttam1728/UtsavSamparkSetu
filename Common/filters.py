from django.contrib import admin

from FolloWUp.models import FollowupStatus, HowMethods

from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from Mandal.models import Karyakram

from SamparkKarykar.models import KaryakarProfile

class KarykarDropdownFilter(admin.SimpleListFilter):
    template = "admin/dropdown_filter.html"
    title = 'Karykar'
    parameter_name = 'Karykar'
    
    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        all_karykars = KaryakarProfile.objects.filter(profile__mandal=request.user.yuvakprofile.mandal)
        query_objs = tuple()
        for karykar in all_karykars.all():
            query_objs += ((karykar.pk,_(karykar.__str__())),)

        return query_objs

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(
                Q(SamparkKarykar__id=self.value())
            )

class HowDropdownFilter(admin.SimpleListFilter):
    template = 'admin/dropdown_filter.html'
    title = 'How'
    parameter_name = 'How'
    
    def lookups(self, request, model_admin):
        return ((status.value, status.name) for status in HowMethods)

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(
                Q(How=self.value())
                )
            
class StatusDropdownFilter(admin.SimpleListFilter):
    template = "admin/dropdown_filter.html"
    title = 'Status'
    parameter_name = 'Status'
    
    def lookups(self, request, model_admin):
        return ((methods.value, methods.name) for methods in FollowupStatus )

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(
                Q(Status=self.value())
            )

class KarykramDropdownFilter(admin.SimpleListFilter):
    template = "admin/dropdown_filter.html"
    title = 'Karykram'
    parameter_name = 'Karykram'
    
    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        all_karykrms = Karyakram.objects.filter(Mandal=request.user.yuvakprofile.mandal).order_by('-Karyakram_date')
        query_objs = tuple()
        for karykrm in all_karykrms.all():
            query_objs += ((karykrm.pk,_(karykrm.__str__())),)

        return query_objs

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(
                Q(Karyakram__id=self.value())
            )

