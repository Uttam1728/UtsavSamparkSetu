"""SamparkSetu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from FolloWUp import views as Followup_view

admin.site.site_header = 'Utsav Sampark Setu'
admin.site.site_title = 'Utsav Sampark Setu'
admin.site.enable_nav_sidebar = False
admin.site.site_url = None
urlpatterns = [
                  path('', lambda request: redirect('admin/', permanent=False)),
                  path('admin/', admin.site.urls),
                  path('mark_present', Followup_view.mark_attandance),
                  path('qr_scan', Followup_view.qr_scan),
                  path(r'advanced_filters/', include('advanced_filters.urls')),
                  path('', include('pwa.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
