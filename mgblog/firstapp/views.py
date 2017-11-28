from django.shortcuts import render, redirect, HttpResponse
from firstapp.models import Article, Comment, Ticket
from firstapp.forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='index')
    context['form'] = form
    return render(request, 'login.html', context)


def index_register(request):
    context = {}
    if request.method == 'GET':
        register_form = UserCreationForm
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect(to='login')
    context['form'] = register_form
    return render(request, 'register.html', context)


def index(request, cate=None):
    # if cate is None:
    article_list = Article.objects.all()
    # else:
    #     article_list = Article.objects.filter(tag='Editors')

    # TODO 完成异常处理。
    #     article_list = Article.objects.all()

    page_robot = Paginator(article_list, 2)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {
        'article_list': article_list
    }
    return render(request, 'index.html', context)


# def detail(request, page_num):
#     """
#     实现了detail页面的渲染，评论的渲染提交显示。但是没有渲染错误信息。
#     """
#     if request.method == "GET":
#         form = CommentForm
#
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             content = form.cleaned_data["content"]
#             article = Article.objects.get(id=page_num)
#             c = Comment(name=name, content=content, belong_to=article)
#             c.save()
#             return redirect(to="detail", page_num=page_num)
#     comment_list = Comment.objects.all()
#     article = Article.objects.get(id=page_num)
#     context = {
#         'article': article,
#         'comment_list': comment_list,
#         'form': form,
#         }
#     return render(request, 'detail.html', context)


# def detail(request, page_num=1):
#     """
#     分离视图。
#     """
#     article = Article.objects.get(id=page_num)
#     if request.method == "GET":
#         form = CommentForm
#     context = {
#         "article": article,
#         "form": form,
#     }
#     return render(request, 'detail.html',context)
#
#
# def comment(request, page_num):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid:
#             name = form.cleaned_data["name"]
#             comment = form.cleaned_data["comment"]
#             article = Article.objects.get(id=page_num)
#             c = Comment(name=name,comment=comment, belong_to=article)
#             c.save()
#             return redirect(to="detail", id=page_num)
#     return redirect(to="detail", page_num=id)


def detail(request, page_num, error_form=None):
    context = {}
    form = CommentForm
    article = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    context['article'] = article

    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    like_counts = Ticket.objects.filter(choice='like', article_id=page_num).count()
    try:
        author_id = request.user.profile.id
        user_ticket_for_this_article = Ticket.objects.get(voter_id=author_id, article_id=page_num)
        context['user_ticket'] = user_ticket_for_this_article
    except AttributeError:
        print('请登陆后投票')
    context['like_count'] = like_counts
    return render(request, 'detail.html', context)


def detail_vote(request, page_num):

    try:
        author_id = request.user.profile.id
        user_ticket_for_this_article = Ticket.objects.get(voter_id=author_id, article_id=page_num)
        user_ticket_for_this_article.choice = request.POST['vote']
        user_ticket_for_this_article.save()
    except AttributeError:
        print('请登陆后投票')
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=author_id, article_id=page_num, choice=request.POST['vote'])
        new_ticket.save()
    return redirect(to='detail', page_num=page_num)


# def detail(request, page_num):
#     context = {}
#     article_info = Article.objects.get(id=page_num)
#     author_id = request.user.profile.id
#     try:
#         user_ticket_for_this_article = Ticket.objects.get(voter_id=author_id, article_id=page_num)
#         context['user_ticket'] = user_ticket_for_this_article
#     except :
#         pass
#     context['article_info'] = article_info
#     return render(request, 'detail.html', context)


def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['content']
        a = Article.objects.get(id=page_num)
        c = Comment(name=name, content=comment, belong_to=a)
        c.save()
    else:
        return detail(request, page_num, error_form=form)
    return redirect(to='detail', page_num=page_num)
