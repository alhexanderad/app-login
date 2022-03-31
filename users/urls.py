from urllib.parse import urlparse
from django.urls import path
from users.views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'users'

urlpatterns = [
    path('change-password', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
]