from django.contrib import admin
from firstapp.models import UserProfile
# Register your models here.
from firstapp.models import Article, Comment
# Ticket


admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Comment)
# admin.site.register(Ticket)