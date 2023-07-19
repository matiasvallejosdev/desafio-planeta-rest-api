from game_api.models import Topic, Game, Slot, Piece
from django.utils import timezone


def create_sample_game(name='My name', subhead='Subhead', summary='', color='green', is_published=True):
    return Game.objects.create(
        name=name,
        subhead=subhead,
        summary=summary,
        color=color,
        slot=Slot.objects.create(name='Slot'),
        is_published=is_published
    )


def create_sample_topic(title='Title', game=None, is_published=True):
    return Topic.objects.create(
        level='easy',
        game=game,
        title=title,
        summary='',
        thumbnail=None,
        featured=False,
        is_published=is_published,
        created_at=timezone.now()
    )
