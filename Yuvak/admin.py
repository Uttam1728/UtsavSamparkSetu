from django.contrib import admin

from Common.util import  Profile_Completion, getMandal, is_member, messageIcons

from django.utils.html import format_html
from Yuvak.models import SatsangProfile, YuvakProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.utils.translation import gettext as _
# method for updating
@receiver(post_save, sender=YuvakProfile)
def Create_SatsangiProfile(sender, instance, **kwargs):
    if not SatsangProfile.objects.filter(yuvakProfile=instance).exists():
        s = SatsangProfile(yuvakProfile=instance)
        s.save()
    username = instance.FirstName.lower() + str(instance.pk).zfill(3)
    email = username + '@' + username + '.com'
    if instance.user is None:
        user = User.objects.create_user(username=username,
                                    email=email,
                                    password='1234', is_staff=True)
        
        group = Group.objects.get(name='Yuvak')
        user.groups.add(group)   
        YuvakProfile.objects.filter(pk=instance.pk).update(user=user)

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
        if groupName is None:
            return queryset
        return queryset.filter(user__groups__name = groupName)

class YuvakProfileAdmin(admin.ModelAdmin):
    
    change_list_template = 'admin/yuvak_change_list.html'
    
    list_display = ("__str__", "Profile_Completion", "WhatsApp","Call","SMS","user")

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
    
    def Profile_Completion(self,obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def MessageIcons(self,obj):
        return format_html(messageIcons(obj.WhatsappNo,27))
    MessageIcons.short_description = 'Connect'

    def get_queryset(self, request):
        qs = super(YuvakProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(mandal=getMandal(request.user))
        elif is_member(request.user,"Sampark Karykar"):
            return YuvakProfile.objects.filter(karyakarprofile__profile__user = request.user)
        elif is_member(request.user,"Yuvak"):
            return qs.filter(pk=request.user.yuvakprofile.pk)
        
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.is_superuser:
            self.list_filter = [RoleFilter]
            if "Role" not in self.list_display:
                 self.list_display += ("Role",)
        else:
            self.list_filter = []
        return super(YuvakProfileAdmin, self).changelist_view(request, extra_context=None)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.readonly_fields = ["user","mandal"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)

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
            return qs.filter(yuvakprofile__mandal=getMandal(request.user))
        else:
            self.list_filter = []
            return qs.filter(pk=request.user.id) 
    
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if not user.is_superuser:
            self.list_filter = []
            self.list_display = ['__str__','email','password']
            self.search_fields = []
            
        return super(UserAdmin, self).changelist_view(request, extra_context=None)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.fieldsets = ((None, {"fields": ("username","password","email")}),)
        
        return super(UserAdmin, self).change_view(request, object_id, extra_context)

class SatsangProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "Profile_Completion",)
    fieldsets = ((None, {"fields": (("NityaPuja","NityaPujaYear"),
    ("TilakChandlo","TilakChandloYear"),
    ("Satsangi","SatsangiYear"),
    ("AthvadikSabha","AthvadikSabhaYear"),
    ("Ravisabha","RavisabhaYear"),
    ("GharSatsang","GharSatsangYear"),
    ("SSP","SSPStage"),
    ("Ekadashi","EkadashiYear"),
    ("Niymit_Vanchan","Niymit_VanchanYear"),
    )}),)
    
    def Profile_Completion(self,obj):
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            Profile_Completion(obj)
        )

    def get_queryset(self, request):
        qs = super(SatsangProfileAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs.filter(yuvakProfile__mandal=getMandal(request.user))
        else:
            return qs.filter(yuvakProfile=request.user.yuvakprofile) 
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.is_superuser:
            self.readonly_fields = ["yuvakProfile"]
        else:
            self.readonly_fields = []
        return super().change_view(request, object_id, form_url, extra_context)

# # Create your models here.
# class User(AbstractUser):
    
#     def set_password(self, raw_password):
#         if self.force_pswd_first_login is None:
#             self.default_pwd_updated = False
#         elif not self.force_pswd_first_login:
#             self.default_pwd_updated = True
#         super().set_password(raw_password)


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(YuvakProfile, YuvakProfileAdmin)
admin.site.register(SatsangProfile,SatsangProfileAdmin)
