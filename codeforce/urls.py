#!/usr/bin/env python
"""
Author:     Zhikai Ding
For:        CS5200 Project CodeForce
version:    "1.0"
"""


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^home/medium/$', views.home_medium, name = 'home_medium'),
    url(r'^home/hard/$', views.home_hard, name = 'home_hard'),
    url(r'^home/logout/$', views.home_logout, name='home_logout'),
    url(r'^problem/(?P<pid>[0-9]+)/$', views.problem_detail, name='problem_detail'),
    url(r'^gotoproblem/$', views.gotoproblem, name='gotoproblem'),
    url(r'^problem_check/(?P<pid>[0-9]+)/$', views.problem_check, name='problem_check'),
    url(r'^problem_check/(?P<cid>[0-9]+)/(?P<pid>[0-9]+)/$', views.contest_problem_check, name='contest_problem_check'),
    url(r'^problem_check/(?P<cid>[0-9]+)/(?P<ocid>[0-9]+)/(?P<pid>[0-9]+)/$', views.check_ongoing, name='check_ongoing'),
    url(r'^contest/$', views.contest, name='contest'),
    url(r'^current_contest/$', views.current_contest, name='current_contest'),
    url(r'^contest_detail/(?P<cid>[0-9]+)/$', views.contest_detail_default, name='contest_detail_default'),
    url(r'^contest_detail/(?P<cid>[0-9]+)/(?P<cpid>[0-9]+)/$', views.contest_detail, name='contest_detail'),
    url(r'^rating/$', views.rating, name='rating'),
    url(r'^rating_test/$', views.rating_test, name='rating_test'),
    url(r'^contest_simulate/(?P<cid>[0-9]+)/$', views.contest_simulate, name='contest_simulate'),
    url(r'^ongoing/(?P<cid>[0-9]+)/(?P<ocid>[0-9]+)/(?P<cpid>[0-9]+)/$', views.ongoing, name='ongoing'),
    url(r'^register/(?P<cid>[0-9]+)/$', views.register, name='register'),
    url(r'^real_contest/(?P<cid>[0-9]+)/$', views.real_contest, name='real_contest'),
    url(r'^contest_rating/(?P<cid>[0-9]+)/$', views.contest_result, name='contest_result'),
    url(r'^submit/(?P<ocid>[0-9]+)/$', views.submit, name='submit'),
#     url(r'^search/$', views.search, name='search'),
#     url(r'^result/$', views.result, name='result'),
#     url(r'^user/$', views.user, name='user'),
#     url(r'^follow/$', views.follow, name='follow'),
#     url(r'^friend/$', views.friend, name='friend'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<uid>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile_edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile_change/(?P<uid>[0-9]+)/$', views.profile_change, name='profile_change'),
    url(r'^search/$', views.search, name='search'),
#     url(r'^setting/$', views.setting, name='setting'),
#     url(r'^about/$', views.about, name='about'),
]