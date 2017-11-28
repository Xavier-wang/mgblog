"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import index, detail
from firstapp.views import index_login, index_register, detail_vote
from django.contrib.auth.views import logout
from firstapp.views import detail_comment


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name="index"),
    url(r'index^(?P<cate>[A-Za-z]+)$', index, name="index"),

    url(r'^login', index_login, name="login"),
    url(r'^register', index_register, name="register"),
    url(r'^logout', logout, {'next_page': '/login'}, name="logout"),

    url(r'^detail/(?P<page_num>\d+)/$', detail, name="detail"),
    url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment, name="comment"),
    url(r'^detail/vote/(?P<page_num>\d+)/$', detail_vote, name="vote"),

]
