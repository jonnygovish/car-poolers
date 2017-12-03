from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

apps_name = 'rider'

urlpatterns = [
  url(r'^$',views.rider, name = 'rider'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )