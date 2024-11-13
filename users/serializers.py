from rest_framework import serializers
from .models import Customuser


class LoginSerializer(serializers.Serializer):
 name = serializers.CharField()
 password = serializers.CharField()

 def validate(self, data):
  name = data.get('name')
  password = data.get('password')

  if not name or not password:
   raise serializers.ValidationError("Заполните поля 'name' и 'password'")

  user = Customuser.objects.filter(name=name).first()
  if user is None:
   raise serializers.ValidationError("Пользователь не найден")

  if not user.check_password(password):
   raise serializers.ValidationError("Неверный пароль")

  return data


class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = Customuser
  fields = ('name', 'email', 'password')
  extra_kwargs = {'password': {'write_only': True}}

 def create(self, validated_data):
  user = Customuser.objects.create_user(
   name=validated_data['name'],
   email=validated_data['email'],
   password=validated_data['password'],
  )
  return user

 def validate_email(self, value):
  if Customuser.objects.filter(email=value).exists():
   raise serializers.ValidationError("Этот адрес электронной почты уже используется.")
  return value


class RegistrationStepTwoSerializer(serializers.Serializer):
 type_mbti = serializers.CharField(max_length=4)

 def validate_type_mbti(self, value):
  if not value.strip():
   raise serializers.ValidationError("type_mbti должно быть не пустой строкой")
  return value