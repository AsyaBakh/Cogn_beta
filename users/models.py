from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
  id_user = models.AutoField(primary_key=True)
  username = models.CharField(max_length=45, blank=True, null=True, unique=True)
  description = models.CharField(max_length=45, blank=True, null=True)
  email = models.CharField(max_length=45, blank=True, null=True)
  password = models.CharField(max_length=45, blank=True, null=True)
  image = models.CharField(max_length=45, blank=True, null=True)
  type_mbti = models.CharField(max_length=4, blank=True, null=True)
  id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role')
  id_mbti_type = models.ForeignKey('MbtiType', models.DO_NOTHING, db_column='id_mbti_type')

  class Meta:
    db_table = 'customuser'

  groups = models.ManyToManyField(
    Group, # Импорт модели Group
    verbose_name='groups',
    blank=True,
    related_name='custom_user_set',
  )
  user_permissions = models.ManyToManyField(
    Permission, # Импорт модели Permission
    verbose_name='user permissions',
    blank=True,
    related_name='custom_user_set',
  )

  def __str__(self):
    return self.username

class Article(models.Model):
    id_article = models.AutoField(primary_key=True)  # The composite primary key (id_article, id_user) found, that is not supported. The first column is selected.
    article_name = models.CharField(max_length=128, blank=True, null=True)
    article_body = models.CharField(max_length=1024, blank=True, null=True)
    id_user = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='id_user')

    class Meta:
        db_table = 'article'
        unique_together = (('id_article', 'id_user'),)


class Articleimages(models.Model):
    article = models.ForeignKey('Articles', models.DO_NOTHING)
    image_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'articleimages'


class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'articles'


class Avatars(models.Model):
    user = models.ForeignKey('CustomUser', models.DO_NOTHING)
    avatar_url = models.CharField(max_length=255)
    date_added = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'avatars'


class Chats(models.Model):
    user = models.ForeignKey('CustomUser', models.DO_NOTHING)

    class Meta:
        db_table = 'chats'


class Friends(models.Model):
    user = models.ForeignKey('CustomUser', models.DO_NOTHING)
    friend = models.ForeignKey('CustomUser', models.DO_NOTHING, related_name='friends_friend_set')
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'friends'


class MbtiQuestion(models.Model):
    id_mbti_question = models.AutoField(primary_key=True)
    question = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'mbti_question'


class MbtiType(models.Model):
    id_mbti_type = models.AutoField(primary_key=True)
    name_of_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'mbti_type'


class Messages(models.Model):
    avatar = models.ForeignKey(Avatars, models.DO_NOTHING)
    message_body = models.TextField()
    chat = models.ForeignKey(Chats, models.DO_NOTHING)
    attachment_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'messages'


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'role'


class Tag(models.Model):
    id_tag = models.AutoField(primary_key=True)
    name_tag = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tag'


class UserTags(models.Model):
    id_tag = models.OneToOneField(Tag, models.DO_NOTHING, db_column='id_tag', primary_key=True)  # The composite primary key (id_tag, id_user) found, that is not supported. The first column is selected.
    id_user = models.ForeignKey('CustomUser', models.DO_NOTHING, db_column='id_user')

    class Meta:
        db_table = 'user_tags'
        unique_together = (('id_tag', 'id_user'),)
