# Generated by Django 4.2.16 on 2024-11-07 20:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.CharField(blank=True, max_length=45, null=True)),
                ('type_mbti', models.CharField(blank=True, max_length=4, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group', verbose_name='groups')),
            ],
            options={
                'db_table': 'customuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_url', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'avatars',
            },
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chats',
            },
        ),
        migrations.CreateModel(
            name='MbtiQuestion',
            fields=[
                ('id_mbti_question', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'mbti_question',
            },
        ),
        migrations.CreateModel(
            name='MbtiType',
            fields=[
                ('id_mbti_type', models.AutoField(primary_key=True, serialize=False)),
                ('name_of_type', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'mbti_type',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(primary_key=True, serialize=False)),
                ('name_role', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id_tag', models.AutoField(primary_key=True, serialize=False)),
                ('name_tag', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.TextField()),
                ('attachment_url', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.avatars')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.chats')),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friends_friend_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'friends',
            },
        ),
        migrations.CreateModel(
            name='Articleimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.articles')),
            ],
            options={
                'db_table': 'articleimages',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_mbti_type',
            field=models.ForeignKey(db_column='id_mbti_type', on_delete=django.db.models.deletion.DO_NOTHING, to='users.mbtitype'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_role',
            field=models.ForeignKey(db_column='id_role', on_delete=django.db.models.deletion.DO_NOTHING, to='users.role'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('article_name', models.CharField(blank=True, max_length=128, null=True)),
                ('article_body', models.CharField(blank=True, max_length=1024, null=True)),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
                'unique_together': {('id_article', 'id_user')},
            },
        ),
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id_tag', models.OneToOneField(db_column='id_tag', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.tag')),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_tags',
                'unique_together': {('id_tag', 'id_user')},
            },
        ),
    ]
