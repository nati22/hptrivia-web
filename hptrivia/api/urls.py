from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from hptrivia_app.views import index
from api.questions.views import QuestionViewSet

router = routers.SimpleRouter()

router.register(r'questions', QuestionViewSet, base_name='questions')

api_urls = router.urls + [
    url(r'^testing', index, name='index'),
]
