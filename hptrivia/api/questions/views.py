from rest_framework import mixins
from rest_framework.exceptions import APIException
from rest_framework.viewsets import GenericViewSet

from hptrivia_app.models import Question

from serializers import QuestionSerializer


class QuestionViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    model = Question
    lookup_field = 'id'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()