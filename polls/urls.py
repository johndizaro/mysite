from django.conf.urls import url
from . import  views


#namespace
app_name = 'polls'
#Agora mudo seu template``polls/index.html`` de:
#polls/templates/polls/index.html

#<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

#para apontar para a view de detalhes do namespace:
#polls/templates/polls/index.html

#<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>




# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]