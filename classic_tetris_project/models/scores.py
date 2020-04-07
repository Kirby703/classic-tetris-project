from django.db import models
from django.utils import timezone

from .users import User

class ScorePB(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=["user", "current"], condition=models.Q(current=True),
                         name="user_current"),
        ]
        constraints = [
            models.UniqueConstraint(fields=["user", "starting_level", "console_type"],
                                    condition=models.Q(current=True),
                                    name="unique_when_current"),
        ]

    TYPE_CHOICES = [
        ("ntsc", "NTSC"),
        ("pal", "PAL"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="score_pbs")

    score = models.IntegerField(null=True, blank=True)
    lines = models.IntegerField(null=True, blank=True)
    starting_level = models.IntegerField(null=True, blank=True)
    console_type = models.CharField(max_length=5, choices=TYPE_CHOICES, default="ntsc", null=False)
    current = models.IntegerField(null=False)

    created_at = models.DateTimeField(null=False, blank=True)

    @staticmethod
    def before_save(sender, instance, **kwargs):
        if instance.id is None:
            instance.created_at = instance.created_at or timezone.now()

models.signals.pre_save.connect(ScorePB.before_save, sender=ScorePB)
