from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #(r'^hello/$', hello),
    (r'^time/$', current_datetime),
    #()为参值, views.py可以创建参数获取
    (r'^time/plus/(\d{1,2})$', hours_ahead),
)
