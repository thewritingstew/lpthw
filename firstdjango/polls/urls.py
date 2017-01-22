from django.conf.urls import url
from . import views

app_name = 'polls'  # provides url namespace for the polls app.
urlpatterns = [
    # index of polls
    # ex: /polls/
    url(r'^$', views.index, name='index'), 
    
    # question detail view
    # the 'name' value can be called by the {% url %} template tag
    # ex: /polls/specifics/5/
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
    # results of question view
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    
    # vote view
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # ex: /polls/ohsnap
    #~ url(r'^ohsnap/$', views.ohsnap, name='ohsnap'),  # polls/ohsnap
]

