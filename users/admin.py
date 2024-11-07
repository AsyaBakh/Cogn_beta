from django.contrib import admin
from .models import  Role, Article, CustomUser, Articles, Articleimages, Tag, UserTags, Avatars, Chats, Friends, MbtiQuestion, MbtiType, Messages

admin.site.register(Role)
admin.site.register(Article)
admin.site.register(CustomUser)
admin.site.register(Articles)
admin.site.register(Articleimages)
admin.site.register(Tag)
admin.site.register(UserTags)
admin.site.register(Avatars)
admin.site.register(Chats)
admin.site.register(Friends)
admin.site.register(MbtiQuestion)
admin.site.register(MbtiType)
admin.site.register(Messages)
# Register your models here.
