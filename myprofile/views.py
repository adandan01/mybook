from django.core.urlresolvers import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Profile


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['first_name', 'last_name']


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')
