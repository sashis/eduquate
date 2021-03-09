from django.urls import include, path
from .views import UserSignUpView, UserEditView

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('edit/', UserEditView.as_view(), name='edit'),
]
