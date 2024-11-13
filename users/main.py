from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, name, email, password):
    if not email:
      raise ValueError('The Email must be set')
    email = self.normalize_email(email)
    user = self.model(name=name, email=email)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, name, email, password):
    return self._create_user(name, email, password)

