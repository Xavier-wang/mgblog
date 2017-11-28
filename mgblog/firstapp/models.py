from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    job = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')


class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICE = (
        ('tech', 'Tech'),
        ('life', 'Life'),
        ('Editors', 'editors'),
    )
    tag = models.CharField(choices=TAG_CHOICE, max_length=100)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.URLField(max_length=100, default="static/images/default.png")
    belong_to = models.ForeignKey(to=Article, related_name='under_comment', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, related_name='voted_tickets')  # 用户
    article = models.ForeignKey(to=Article, related_name='tickets')  # 文章
    VOTE_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)

