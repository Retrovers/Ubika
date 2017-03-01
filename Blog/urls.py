"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from. import views

urlpatterns = [
    ##Other
    url(r'^admin/', admin.site.urls, name = "admin"),
    url(r'^jouer',views.Jouer,name = "jouer"),

    ## Blog
    url(r'^blog/view/(?P<slug>[-\w]+)/$', views.BlogView, name = 'blog_view'),
    url(r'^blog',views.BlogList,name = "blog_list"),
    ##User
    url(r'^user/logout', views.UserLogout, name="user_logout"),
    url(r'^user/login', views.UserLogin, name="user_login"),
    url(r'^user/register', views.UserRegister, name="user_register"),
    url(r'^user/setting', views.UserSetting, name="user_setting"),
    
    ##Index
    url(r'^', views.Index, name= "index"),
]
