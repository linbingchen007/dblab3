from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dblab3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$','mysite.views.index',name='index'),
    url(r'^mv/',include('mysite.urls',namespace='mysite')),
]
