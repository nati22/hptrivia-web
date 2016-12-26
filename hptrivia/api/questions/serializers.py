from rest_framework import serializers
from hptrivia_app.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'correct_answer_text',
            'wrong_answer1_text',
            'wrong_answer2_text',
            'wrong_answer3_text'
        )
