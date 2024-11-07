from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserSerializer, LoginSerializer, RegistrationStepTwoSerializer
from .models import CustomUser

#Регистрация
class RegistrationStepOne(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      token, created = Token.objects.get_or_create(user=serializer.instance)
      return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

class RegistrationStepTwo(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def post(self, request, format=None):
    serializer = RegistrationStepTwoSerializer(data=request.data)
    if serializer.is_valid():
      user = request.user
      type_mbti = serializer.validated_data['type_mbti']

      user.type_mbti = type_mbti
      user.save()

      return Response({'message': 'Регистрация завершена'}, status=status.HTTP_200_OK)


# Вход в систему
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = CustomUser.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Неправильный пароль'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
