from rest_framework import serializers
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
 name = serializers.CharField()
 password = serializers.CharField()

 def validate(self, data):
  username = data.get('username')
  password = data.get('password')

  if not username or not password:
   raise serializers.ValidationError("Заполните поля 'username' и 'password'")

  user = CustomUser.objects.filter(username=username).first()
  if user is None:
   raise serializers.ValidationError("Пользователь не найден")

  if not user.check_password(password):
   raise serializers.ValidationError("Неверный пароль")

  return data


class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = CustomUser
  fields = ('username', 'email', 'password')
  extra_kwargs = {'password': {'write_only': True}}

 def create(self, validated_data):
  user = CustomUser.objects.create_user(
   username=validated_data['username'],
   email=validated_data['email'],
   password=validated_data['password'],
  )
  return user

 def validate_email(self, value):
  if CustomUser.objects.filter(email=value).exists():
   raise serializers.ValidationError("Этот адрес электронной почты уже используется.")
  return value


class RegistrationStepTwoSerializer(serializers.Serializer):
 type_mbti = serializers.CharField(max_length=4)

 def validate_type_mbti(self, value):
  if not value.strip():
   raise serializers.ValidationError("type_mbti должно быть не пустой строкой")
  return value