from django.urls import path
from .views import profile, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', profile, name='user-profile')
]