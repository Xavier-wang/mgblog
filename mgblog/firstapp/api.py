# from firstapp.models import Article
# from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # 实际上这就是一个视图函数
# # 先进行序列化,   序列化器，仿照了django的表单.
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:     # 没必要纠结，这就是一个类,来展示用到甚么对象。
#         model = Article
#         fields = '__all__'
#
#
# # 这就是一个api的视图函数.转化为可以返回json的视图.。
# @api_view(['GET'])
# def article(request):
#     article_list = Article.objects.all()
#     serializer = ArticleSerializer(article_list, many=True)
#     return Response(serializer.data)
#
