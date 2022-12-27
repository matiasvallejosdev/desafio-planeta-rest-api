from django.test import TestCase
from django.utils import timezone

from trivia_api.models import Answer, Question, Trivia
from game_api.tests.test_sample import create_sample_topic


class ModelTestCase(TestCase):
    def test_answer_str(self):
        answer = Answer.objects.create(
            answer='my answer',
            is_correct=True
        )
        self.assertIn(answer.answer, str(answer))

    def test_question_str(self):
        question = Question.objects.create(
            question = 'my question',
            type='FourAnswers',
            has_explication = False,
            explication='',
            is_published=True,
            created_at=timezone.now()
        )
        question.answers.add(Answer.objects.create(
            answer='my answer',
            is_correct=True
        ))
        self.assertIn(question.question, str(question))

    def test_trivia_str(self):
        trivia = Trivia.objects.create(
            topic=create_sample_topic(),
            is_published=False,
            created_at=timezone.now()
        )
        trivia.questions.add(Question.objects.create(
            question = 'my question',
            type='FourAnswers',
            has_explication = False,
            explication='',
            is_published=True,
            created_at=timezone.now()
        ))
        self.assertIn(str(trivia.id), str(trivia))