from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^about/$', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    url(r'^drafts/$', views.draft_list, name='draft_list'),
    url('^$', views.post_list, name='post_list'),
]

