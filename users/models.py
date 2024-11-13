# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    article_name = models.CharField(max_length=128, blank=True, null=True)
    article_body = models.CharField(max_length=1024, blank=True, null=True)
    id_user = models.ForeignKey('Customuser', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'article'


class ArticleImages(models.Model):
    article = models.ForeignKey(Article, models.DO_NOTHING)
    image_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'article_images'


class Avatars(models.Model):
    user = models.ForeignKey('Customuser', models.DO_NOTHING)
    avatar_url = models.CharField(max_length=255)
    date_added = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avatars'


class Chats(models.Model):
    user = models.ForeignKey('Customuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chats'


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


class Customuser(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    type_mbti = models.CharField(max_length=4, blank=True, null=True)
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role')
    id_mbti_type = models.ForeignKey('MbtiType', models.DO_NOTHING, db_column='id_mbti_type')
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'customuser'

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
    )


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Friends(models.Model):
    user = models.ForeignKey(Customuser, models.DO_NOTHING)
    friend = models.ForeignKey(Customuser, models.DO_NOTHING, related_name='friends_friend_set')
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friends'

class Likes(models.Model):
    user = models.ForeignKey(Customuser, models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)
    liked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'


class MbtiQuestion(models.Model):
    id_mbti_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mbti_question'


class MbtiType(models.Model):
    id_mbti_type = models.AutoField(primary_key=True)
    name_of_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mbti_type'


class Messages(models.Model):
    avatar = models.ForeignKey(Avatars, models.DO_NOTHING)
    message_body = models.TextField()
    chat = models.ForeignKey(Chats, models.DO_NOTHING)
    attachment_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    post_body = models.CharField(max_length=1024, blank=True, null=True)
    id_user = models.ForeignKey(Customuser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'post'


class PostImages(models.Model):
    post = models.ForeignKey(Post, models.DO_NOTHING)
    image_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'post_images'


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Tag(models.Model):
    id_tag = models.AutoField(primary_key=True)
    name_tag = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class UserTags(models.Model):
    id_user_tags = models.AutoField(primary_key=True)
    id_tag = models.ForeignKey(Tag, models.DO_NOTHING, db_column='id_tag')
    id_user = models.ForeignKey(Customuser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'user_tags'
