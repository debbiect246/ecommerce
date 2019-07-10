from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.urls import path

urlpatterns = [
    path(
        'accounts/password_reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),

]
