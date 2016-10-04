from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.ProfileList.as_view(), name='profile-list'),
    url(r'profile/add/$', views.ProfileCreate.as_view(), name='profile-add'),
    url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
]