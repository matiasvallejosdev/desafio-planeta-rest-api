from django.db import models
from django.utils import timezone


class Slot(models.Model):
    name = models.CharField(blank=True, max_length=240)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.name} 📑 {self.image}"


class Piece(models.Model):
    name = models.CharField(blank=True, max_length=240)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.name} 📑 {self.image}"


class Game(models.Model):
    COLOR_CHOICES = (
        ('green', 'GREEN'),
        ('blue', 'BLUE'),
        ('red', 'RED'),
        ('orange', 'ORANGE'),
    )
    name = models.CharField(blank=True, max_length=240)
    subhead = models.CharField(blank=True, max_length=45)
    summary = models.CharField(blank=True, max_length=240)
    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    slot = models.ForeignKey(Slot, blank=True, null=True, on_delete=models.CASCADE)
    pieces = models.ManyToManyField(Piece, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        pieces_count = self.pieces.count()
        slot_count = 0 if self.slot is None else 1
        published = '👍' if self.is_published else '👎'
        return f"{published} → {self.name} 👉 {slot_count} slot and {pieces_count} pieces"


class Topic(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'EASY'),
        ('medium', 'MEDIUM'),
        ('hard', 'HARD')
    )
    level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='easy')
    game = models.ForeignKey(Game, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    summary = models.CharField(blank=True, max_length=150)
    thumbnail = models.ImageField(blank=True, null=True)
    featured = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        published = '👍' if self.is_published else '👎'
        return f"{published} → 📍 {self.title} 🎚️ {str(self.level).capitalize()}"
