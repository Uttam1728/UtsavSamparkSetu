from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html

from Common.util import getMandal, is_member, messageIcons, Profile_Completion
from SamparkKarykar.models import KaryakarProfile


@receiver(post_save, sender=KaryakarProfile)
def Add_KaryKarGroup(sender, instance, **kwargs):
    if instance.karykar1profile:
        user = instance.karykar1profile.user
        if not user.groups.filter(name="Sampark Karykar").exists():
            group = Group.objects.get(name='Sampark Karykar')
            user.groups.add(group)
    if instance.karykar2profile:
        user = instance.karykar2profile.user
        if not user.groups.filter(name="Sampark Karykar").exists():
            group = Group.objects.get(name='Sampark Karykar')
            user.groups.add(group)


class KaryakarProfileAdmin(admin.ModelAdmin):
    # change_list_template = 'admin/karykar_change_list.html'
    list_display = ("__str__", "Karykar_1_image", "Karykar_1", "Karykar_2_image", "Karykar_2", "Yuvak_List")
    list_per_page = 20
    autocomplete_fields = ('karykar1profile', 'karykar2profile', 'Yuvaks')
    search_fields = ('karykar1profile__FirstName__icontains',
                     'karykar1profile__SurName__icontains',
                     'karykar2profile__FirstName__icontains',
                     'karykar2profile__SurName__icontains',
                     'Yuvaks__FirstName__icontains',
                     'Yuvaks__SurName__icontains')

    def Karykar_1(self, obj):
        if obj.karykar1profile:
            return format_html(
                obj.karykar1profile.FirstName + " " + obj.karykar1profile.SurName + " <br> " + messageIcons(
                    obj.karykar1profile.WhatsappNo, 20, False))
        return ''

    def Karykar_1_image(self, obj):
        if obj.karykar1profile:
            if obj.karykar1profile.ProfilePhoto:
                s = '<img src={} height="80px" width="80px" style="border-radius: 50%;border: 1px solid black" alt="profilepic"/></div>'.format(
                    obj.karykar1profile.ProfilePhoto.url)
            else:
                s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        else:
            s = ''
        return format_html(s)

    Karykar_1_image.short_description = ""

    def Karykar_2(self, obj):
        if obj.karykar2profile:
            return format_html(
                obj.karykar2profile.FirstName + " " + obj.karykar2profile.SurName + " <br> " + messageIcons(
                    obj.karykar2profile.WhatsappNo, 20, False))
        return ''

    def Karykar_2_image(self, obj):
        if obj.karykar2profile:
            if obj.karykar2profile.ProfilePhoto:
                s = '<img src={} height="80px" width="80px" style="border-radius: 50%;border: 1px solid black" ' \
                    'alt="profilepic"/></div>'.format(
                    obj.karykar2profile.ProfilePhoto.url)
            else:
                s = '<img  height="80px" width="80px" src="/static/img/yuvak.png" >'
        else:
            s = ''
        return format_html(s)

    Karykar_2_image.short_description = ""

    def Yuvak_List(self, obj):
        s = ''
        if not self.request.user.is_superuser:
            if not is_member(self.request.user, "Sampark Karykar"):
                yuvak = self.request.user.yuvakprofile
                profile_completion_yuvak = Profile_Completion(yuvak)
                profile_completion_satsangi = Profile_Completion(yuvak.satsangprofile)
                s += '<li>{} {} <progress value="{}" style="width:65px" max="100"></progress><span style="font-size:12px"> {}%  </span><progress value="{}" style="width:65px"  max="100"></progress><span style="font-size:12px" > {}%</span></li>'.format(
                    yuvak.FirstName, yuvak.SurName, profile_completion_yuvak,
                    profile_completion_yuvak, profile_completion_satsangi,
                    profile_completion_satsangi)
                return format_html(s)

        for yuvak in obj.Yuvaks.all():
            profile_completion_yuvak = Profile_Completion(yuvak)
            profile_completion_satsangi = Profile_Completion(yuvak.satsangprofile)
            s += '<li>{} {} <progress value="{}" style="width:65px" max="100"></progress><span style="font-size:12px"> {}%  </span><progress value="{}" style="width:65px"  max="100"></progress><span style="font-size:12px" > {}%</span></li>'.format(
                yuvak.FirstName, yuvak.SurName, profile_completion_yuvak,
                profile_completion_yuvak, profile_completion_satsangi,
                profile_completion_satsangi)  # + messageIcons(yuvak.WhatsappNo,20)
        return format_html(s)

    Yuvak_List.short_description = "___________________________Yuvak List____________________________."

    def get_search_fields(self, request):
        if not request.user.is_superuser:
            if not is_member(request.user, "Sampark Karykar"):
                return []
        return super().get_search_fields(request)

    def get_queryset(self, request):
        self.request = request
        qs = super(KaryakarProfileAdmin, self).get_queryset(request)
        mandal = getMandal(request.user)
        if request.user.is_superuser:
            return qs.filter(Q(karykar1profile__mandal=mandal) | Q(karykar2profile__mandal=mandal))
        elif is_member(request.user, "Sampark Karykar"):
            return qs.filter(
                Q(karykar1profile=request.user.yuvakprofile) | Q(karykar2profile=request.user.yuvakprofile))
        elif is_member(request.user, "Yuvak"):
            return request.user.yuvakprofile.karyakarprofile_set

    def get_readonly_fields(self, request, obj):
        if not request.user.is_superuser:
            return ["Yuvaks", "karykar1profile", "karykar2profile", "mandal"]
        return super().get_readonly_fields(request, obj)


# Register your models here.
admin.site.register(KaryakarProfile, KaryakarProfileAdmin)
