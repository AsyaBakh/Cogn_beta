from django.urls import path
from .views import LoginView, RegistrationStepOne, RegistrationStepTwo

urlpatterns = [
    path('register/', RegistrationStepOne.as_view(), name='register'),
    path('register_mbti/', RegistrationStepTwo.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='LoginView'),
]
try:
    # Здесь ваш код, который может вызвать ошибку при доступе к базе данных
    from django.contrib.auth.models import User
    user = User.objects.get(username='admin')
    # ...
except Exception as e:
    print(e)
    urlpatterns = []