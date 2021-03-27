from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from apps.account.forms import ProfileForm


class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            url_params = urlencode({REDIRECT_FIELD_NAME: reverse('profile')})
            return redirect(settings.LOGIN_URL + '?' + url_params)  # noqa: WPS336
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
