from django.db import models


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
    name = models.CharField(blank=True, max_length=240)
    subhead = models.CharField(blank=True, max_length=45)
    summary = models.CharField(blank=True, max_length=240)
    slot = models.ForeignKey(Slot, blank=True, null=True, on_delete=models.CASCADE)
    pieces = models.ManyToManyField(Piece, blank=True)

    def __str__(self):
        pieces_count = self.pieces.count()
        slot_count = 0 if self.slot is None else 1
        text = f"{self.name} 👉 {slot_count} slot and {pieces_count} pieces"
        return text


class Topic(models.Model):
    COLOR_CHOICES = (
        ('green', 'GREEN'),
        ('blue', 'BLUE'),
        ('red', 'RED'),
        ('orange', 'ORANGE'),
        ('black', 'BLACK'),
    )
    game = models.ForeignKey(Game, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.CharField(blank=True, max_length=240)
    thumbnail = models.ImageField(blank=True, null=True)
    thumbnail_color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='black')
    featured = models.BooleanField(default=False, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        published = '👍' if self.is_published else '👎'
        text = f"{published} →   {self.game.name} 📍 {self.title}"
        return text
