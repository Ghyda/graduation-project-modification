from django.conf.urls import url

from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/answers/$', views.AnswersView.as_view(), name='answers'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.VoteView, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/new/$', views.create_question, name='create_question'),
    url(r'^(?P<question_id>[0-9]+)/question_edition/$', views.edit_question, name='edit_question'),
    url(r'^(?P<question_id>[0-9]+)/question_deletion/$', views.delete_question, name='question_deletion'),
    url(r'^(?P<question_id>[0-9]+)/answer_edit/$', views.edit_answer, name='edit_answer'),
    url(r'^(?P<question_id>[0-9]+)/comment_edit/$', views.edit_comment, name='edit_comment'),

]
