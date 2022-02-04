from urllib import request
from django.contrib import admin

from django import forms
from django.contrib.admin.helpers import ActionForm
from Common.util import is_member
from Mandal.models import Karyakram

from Yuvak.models import YuvakProfile
from FolloWUp.models import HowMethods
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class RoleFilter(admin.SimpleListFilter):
    title = 'Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('Sampark Karykar', 'Sampark Karykar'),
            ('Yuvak',  'Yuvak'),
        )

    def queryset(self, request, queryset):
        groupName = self.value()
        print(groupName, "GroupName")
        if groupName is None:
            return queryset
        return queryset.filter(user__groups__name = groupName)

        # if groupName == 'Yuvak':
        #     return queryset.filter(Q(message__isnull=True) | Q(message__exact=''))


class YuvakProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "WhatsappNo","user","Role")

    def get_queryset(self, request):
        qs = super(YuvakProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            # self.list_display+= ("Groups",)
            return qs
        elif is_member(request.user,"Yuvak"):
            return qs.filter(user=request.user)
        elif is_member(request.user,"Sampark Karykar"):
            return YuvakProfile.objects.filter(karyakarprofile__user = request.user)

    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.is_superuser:
            self.list_filter = [RoleFilter]
        else:
            self.list_filter = []
        return super(YuvakProfileAdmin, self).changelist_view(request, extra_context=None)


    def Role(self,obj):
        group_names = []
        for g in obj.user.groups.all():
            group_names.append(g.name)
        return ",".join(group_names)

        

class UserAdmin(AuthUserAdmin):
    
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        else:
            self.list_filter = []
            return qs.filter(pk=request.user.id) 
            


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(YuvakProfile, YuvakProfileAdmin)

