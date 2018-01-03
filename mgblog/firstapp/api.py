from .serirializer import ArticleSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Article
from rest_framework.response import  Response

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


@api_view(['GET'])
def ArticleListView(request):
    article_list = Article.objects.order_by('-id')
    if request.method == 'GET':
        serializer = ArticleSerializer(article_list, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     return Response(404)
