
from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext as _, gettext_lazy
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect


class NewLoginView(LoginView):
    def get_redirect_url(self):
        if self.request.method == "POST" and self.request.user.get_username()\
                and not self.request.user.yuvakprofile.yuvakprofile.force_pswd_first_login:
            redirect_to = reverse("admin:password_change")
        else:
            redirect_to = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name, '')
            )
        return redirect_to


class NewAdminSite(AdminSite):
    site_header = site_title = gettext_lazy("Sampark Setu Admin ")

    def __init__(self, name="admin"):
        super().__init__(name)

    @never_cache
    def login(self, request, extra_context=None):
        """
        Display the login form for the given HttpRequest.
        """
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            if request.user.get_username() and not request.user.yuvakprofile.force_pswd_first_login:
                # default password not changed, force to password_change view
                path = reverse('admin:password_change', current_app=self.name)
            else:
                path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(path)

        from django.contrib.auth.views import LoginView
        from django.contrib.admin.forms import AdminAuthenticationForm
        context = {
            **self.each_context(request),
            'title': _('Log in'),
            'app_path': request.get_full_path(),
            'username': request.user.get_username(),
        }
        if (REDIRECT_FIELD_NAME not in request.GET and
                REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('admin:index', current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'admin/login.html',
        }
        request.current_app = self.name
        return NewLoginView.as_view(**defaults)(request) # use NewLoginView

    @never_cache
    def index(self, request, extra_context=None):
        if request.user.get_username() and not request.user.yuvakprofile.force_pswd_first_login:
            # if default password not updated, force to password_change page
            context = self.each_context(request)
            context.update(extra_context or {})
            return self.password_change(request, context)
        return super().index(request, extra_context)
    
    
    def using_default_password(self, request):
        if self.has_permission(request) and request.user.get_username() and not request.user.yuvakprofile.force_pswd_first_login:
                return True
        return False

    def each_context(self, request):
        context = super().each_context(request)
        context["force_pwd_change"] = self.using_default_password(request)
        return context


admin_site = NewAdminSite(name="admin")
