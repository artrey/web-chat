from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.account.forms import ProfileForm


class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
