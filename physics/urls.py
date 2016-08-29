from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^experimental/$', views.experimental, name='experimental'),
    url(r'^theoretical/$', views.theoretical, name='theoretical'),
    url(r'^authenticate/$', views.authenticate_user, name='authenticate_user'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^contact/$', views.contact, name='contact'),
    
    url(r'^upload/topic$', views.topic, name='topic'),
    url(r'^upload/topic/edit/(?P<topic_id>[0-9]+)/$', views.add_edit_topic, name='edit_topic'),
    url(r'^upload/topic/new/$', views.add_edit_topic, name='add_topic'),
    url(r'^upload/topic/delete/(?P<topic_id>[0-9]+)/$', views.delete_topic, name='delete_topic'),

    url(r'^upload/lecture$', views.lecture, name='lecture'),
    url(r'^upload/lecture/edit/(?P<lecture_id>[0-9]+)/$', views.add_edit_lecture, name='edit_lecture'),
    url(r'^upload/lecture/new/$', views.add_edit_lecture, name='add_lecture'),
    url(r'^upload/lecture/delete/(?P<lecture_id>[0-9]+)/$', views.delete_lecture, name='delete_lecture'),
    
    url(r'^upload/pset$', views.pset, name='pset'),
    url(r'^upload/pset/edit/(?P<pset_id>[0-9]+)/$', views.add_edit_pset, name='edit_pset'),
    url(r'^upload/pset/new/$', views.add_edit_pset, name='add_pset'),
    url(r'^upload/pset/delete/(?P<pset_id>[0-9]+)/$', views.delete_pset, name='delete_pset'),
    
    url(r'^upload/announcement$', views.announcement, name='announcement'),
    url(r'^upload/announcement/edit/(?P<announcement_id>[0-9]+)/$', views.add_edit_announcement, name='edit_announcement'),
    url(r'^upload/announcement/new/$', views.add_edit_announcement, name='add_announcement'),
    url(r'^upload/announcement/delete/(?P<announcement_id>[0-9]+)/$', views.delete_announcement, name='delete_announcement'),
    
    
    url(r'^upload/news$', views.news, name='news'),
    url(r'^upload/news/edit/(?P<news_id>[0-9]+)/$', views.add_edit_news, name='edit_news'),
    url(r'^upload/news/new/$', views.add_edit_news, name='add_news'),
    url(r'^upload/news/delete/(?P<news_id>[0-9]+)/$', views.delete_news, name='delete_news'),
    
    url(r'^upload/topic_requests$', views.topic_requests, name='topic_requests'),
    url(r'^upload/topic_requests/view/(?P<topic_request_id>[0-9]+)/$', views.view_topic_request, name='view_topic_request'),
    url(r'^upload/topic_requests/delete/(?P<topic_request_id>[0-9]+)/$', views.delete_topic_request, name='delete_topic_request'),
    
    url(r'^upload/suggestions$', views.suggestions, name='suggestions'),
    url(r'^upload/suggestions/view/(?P<suggestion_id>[0-9]+)/$', views.view_suggestion, name='view_suggestion'),
    url(r'^upload/suggestions/delete/(?P<suggestion_id>[0-9]+)/$', views.delete_suggestion, name='delete_suggestion'),
]