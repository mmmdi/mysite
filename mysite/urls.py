"""mysite URL Configuration

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
from blog import views as blog_views
# from django.login import views as login_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',blog_views.home),
    url(r'^home/$',blog_views.home),
    url(r'^register/$',blog_views.register),  
    url(r'^login/$',blog_views.login),  
    url(r'^logout/$',blog_views.logout),
    url(r'^share/$',blog_views.share),
    url(r'^share_form/$',blog_views.share_form,name="share_form"),
    url(r'^make/$',blog_views.make),
    url(r'^plan_form/$',blog_views.plan_form,name="plan_form"),
    url(r'^u/(\d*)$',blog_views.userhome),
    url(r'^plan/(\d*)$',blog_views.plan),
    url(r'^article/(\d*)$',blog_views.article),
    url(r'^edit/$',blog_views.edit,name="edit"),
    url(r'^editsubmit/(\d*)/(\d*)$',blog_views.editsubmit),
    url(r'^fvplan/(\d*)/(\d*)$',blog_views.fvplan),
    url(r'^fvarticle/(\d*)/(\d*)$',blog_views.fvarticle),
    url(r'^fvcase/(\d*)/(\d*)$',blog_views.fvcase),
    url(r'^search/$',blog_views.search),
    # url(r'^changepwd/$',blog_views.changePwd),  
]
