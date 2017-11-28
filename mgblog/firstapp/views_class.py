# from django.shortcuts import render, redirect, HttpResponse
# from firstapp.models import Article, Comment, Ticket
# from firstapp.forms import CommentForm, LoginForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.core.exceptions import ObjectDoesNotExist
#
# # Create your views here.
#
# from django.views.generic
#
#
# def index_login(request):
#     context = {}
#     if request.method == 'GET':
#         form = AuthenticationForm
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect(to='index')
#     context['form'] = form
#     return render(request, 'login.html', context)
#
#
# def index_register(request):
#     context = {}
#     if request.method == 'GET':
#         register_form = UserCreationForm
#     if request.method == 'POST':
#         register_form = UserCreationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             return redirect(to='login')
#     context['form'] = register_form
#     return render(request, 'register.html', context)
#
#
# def index(request, cate=None):
#     context = {}
#     # if cate is None:
#     article_list = Article.objects.all()
#     # if cate == 'editors':
#     #     article_list = Article.objects.filter(tag=True)
#     # else:
#     #     article_list = Article.objects.all()
#
#     page_robot = Paginator(article_list, 6)
#     page_num = request.GET.get('page')
#     try:
#         article_list = page_robot.page(page_num)
#     except EmptyPage:
#
#         article_list = page_robot.page(page_robot.num_pages)
#     except PageNotAnInteger:
#
#         article_list = page_robot.page(1)
#     context['article_list'] = article_list
#
#     return render(request, 'index.html', context)
#
# # def detail(request, page_num):
# #
# #     if request.method == "GET":
# #         form = CommentForm
# #
# #     if request.method == "POST":
# #         form = CommentForm(request.POST)
# #         if form.is_valid():
# #             name = form.cleaned_data["name"]
# #             content = form.cleaned_data["content"]
# #             a = Article.objects.get(id=page_num)
# #             c = Comment(name=name, content=content, belong_to=a)
# #             c.save()
# #             return redirect(to="detail",page_num=page_num)
# #
# #
# # #    comment_list = Comment.objects.all()
# #     article = Article.objects.get(id=page_num)
# #     context['article'] = article
# #  #   context['comment_list'] = comment_list
# #     context['form'] = form
# #
# #     return render(request, 'detail.html', context)
#
# def detail(request, page_num, error_form=None):
#     context = {}
#     form = CommentForm
#     article = Article.objects.get(id=page_num)
#     best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     context['article'] = article
#
#     if error_form is not None:
#         context['form'] = error_form
#     else:
#         context['form'] = form
#
#     article_info = Article.objects.get(id=page_num)
#     author_id = request.user.profile.id
#     like_counts = Ticket.objects.filter(choice='like', article_id=page_num).count()
#     try:
#         user_ticket_for_this_article = Ticket.objects.get(voter_id=author_id, article_id=page_num)
#         context['user_ticket'] = user_ticket_for_this_article
#     except ValueError:
#         pass
#     context['article_info'] = article_info
#     context['like_count'] = like_counts
#     return render(request, 'detail.html', context)
#
#
# def detail_vote(request, page_num):
#     author_id = request.user.profile.id
#     try:
#         user_ticket_for_this_article = Ticket.objects.get(voter_id=author_id, article_id=page_num)
#         user_ticket_for_this_article.choice = request.POST['vote']
#         user_ticket_for_this_article.save()
#     except ObjectDoesNotExist:
#         new_ticket = Ticket(voter_id=author_id, article_id=page_num, choice=request.POST['vote'])
#         new_ticket.save()
#     return redirect(to='detail', page_num=page_num)
#
# # def detail(request, id):
# #     context = {}
# #     article_info = Article.objects.get(id=id)
# #     author_id = request.user.profile.id
# #     print(author_id)
# #     try:
# #         user_ticket_for_this_article = Ticket.objects.get(vote=author_id, article_id=id)
# #         context['user_ticket'] = user_ticket_for_this_article
# #     except PageNotAnInteger:
# #         pass
# #     context['article_info'] = article_info
# #     return render(request, 'detail.html', context)
#
#
# def detail_comment(request, page_num):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         name = form.cleaned_data['name']
#         comment = form.cleaned_data['content']
#         a = Article.objects.get(id=page_num)
#         c = Comment(name=name, content=comment, belong_to=a)
#         c.save()
#     else:
#         return detail(request, page_num, error_form=form)
#     return redirect(to='detail', page_num=page_num)
