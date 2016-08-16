from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$',views.post_list,name = 'post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
    url(r'^post/new/$',views.post_new, name = 'post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit, name = 'post_edit'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.login, name ='login'),
    url(r'^sign_up_ok/$', TemplateView.as_view(template_name = 'mysite/sign_up_ok.html'),name = 'sign_up_ok'),

]






