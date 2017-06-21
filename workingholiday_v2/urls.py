"""workingholiday_v2 URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from workingholiday import views
from django.conf.urls import include
from django.conf import settings

test = views.Views()

urlpatterns = [
    url(r'^$', test.homepage),
    url(r'^search/(?P<area>\w+)',test.searchpage, name="area"),
    url(r'^nodata/$',test.nodata),
    url(r'^useredit/(?P<userid>\d+)/$',test.useredit, name='getid'),
    url(r'^userpage/(?P<uid>\d+)/$',test.userpage, name='user'),
    url(r'^usermanage/(?P<usermanageid>\d+)/', test.usermanage, name='usermanageid'),
    

    url(r'^hostpage/(?P<pageid>\d+)/',test.hostpage, name='pageid'),
    url(r'^hostedit/(?P<hostid>\d+)/',test.hostedit, name="hostid"),
    url(r'^hostmanage/(?P<hostmanageid>\d+)/', test.hostmanage, name='hostmanageid'),
 
    url(r'^admin/', admin.site.urls),

        
    url(r'^getuserid/$',test.getuserid),
    url(r'^getconfirm/$',test.getuserid),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

