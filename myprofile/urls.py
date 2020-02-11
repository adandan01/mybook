from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile-list'),
    path('profile/add/', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    path('profile/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    path('profile/<int:pk>', views.ProfileDelete.as_view(), name='profile-delete'),
]
