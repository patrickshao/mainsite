from django.conf.urls import patterns, url
from aspc.askasagehen.views import home, question

urlpatterns = patterns('',
	url(r'^question/(?P<question_id>\d+)?(/)?', question, name="question_detail"), # /question/123
	url(r'question', question, {'question_id': None}, name='submit_question'), # /question
	url(r'', home, name='askasagehen') # /
)