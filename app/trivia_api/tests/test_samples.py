from trivia_api.models import Trivia, Question, Answer
from django.utils import timezone


def create_sample_trivia(topic=None, is_published=True):
    return Trivia.objects.create(
        topic=topic,
        is_published=is_published,
    )


def create_sample_question(question='question', is_published=True):
    return Question.objects.create(
        question=question,
        type='FourAnswers',
        is_published=is_published,
        created_at=timezone.now()
    )
