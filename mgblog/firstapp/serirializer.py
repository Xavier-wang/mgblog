from .models import Article, People, UserProfile, User, Comment, Ticket
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1)
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

