from urllib import request
from django.contrib import admin

from django import forms
from django.contrib.admin.helpers import ActionForm
from Common.util import getLatestKarykram, is_member, messageIcons
from Mandal.models import Karyakram

from django.utils.html import format_html
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


class YuvakProfileAdmin(admin.ModelAdmin):
    
    change_list_template = 'admin/yuvak_change_list.html'
    
    list_display = ("__str__", "WhatsApp","Call","SMS","user")

    def WhatsApp(self,obj):
        buttons = ''
        buttons += "<a href='https://wa.me/+91{}' ><i class='fa fa-whatsapp' style='font-size:30px;color:green'></i></a>".format(obj.WhatsappNo)
        return format_html(buttons)

    def Call(self,obj):
        buttons = ''
        buttons += "<a href='tel:+91{}'> <i class='fa fa-volume-control-phone' style='font-size:27px;color:deepskyblue;'></i> </a>".format(obj.WhatsappNo)
        return format_html(buttons)
    
    def SMS(self,obj):
        buttons = ''
        buttons += "<a href='sms:+91{}'> <i class='fa fa-commenting-o' style='font-size:27px;color:lightblue;'></i> </a>".format(obj.WhatsappNo)  
        return format_html(buttons)
    
    
    def MessageIcons(self,obj):
        return format_html(messageIcons(obj.WhatsappNo,27))
    MessageIcons.short_description = 'Connect'

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
            self.list_display += ("Role",)
        else:
            self.list_filter = []
        return super(YuvakProfileAdmin, self).changelist_view(request, extra_context=None)

    def Role(self,obj):
        group_names = []
        for g in obj.user.groups.all():
            group_names.append(g.name)
        return ",".join(group_names)

        

class UserAdmin(AuthUserAdmin):
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        else:
            self.list_filter = []
            return qs.filter(pk=request.user.id) 
    
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if not user.is_superuser:
            self.list_filter = []
            self.list_display = ['__str__']
            self.search_fields = []
            
        return super(UserAdmin, self).changelist_view(request, extra_context=None)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.fieldsets = ((None, {"fields": ("username","password")}),)
        return super(UserAdmin, self).change_view(request, object_id, extra_context)
            


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(YuvakProfile, YuvakProfileAdmin)

