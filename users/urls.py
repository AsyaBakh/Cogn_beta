from django.urls import path
from .views import LoginView, RegistrationStepOne, RegistrationStepTwo

urlpatterns = [
    path('register/', RegistrationStepOne.as_view(), name='register'),
    path('register_mbti/', RegistrationStepTwo.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='LoginView'),
]