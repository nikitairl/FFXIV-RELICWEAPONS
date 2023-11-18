from django.db import models
from tinymce.models import HTMLField


class RelicWeapon(models.Model):
    relic_type = models.CharField(max_length=100)
    weapon_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.ImageField(
        upload_to='relics/',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.weapon_name


class Quest(models.Model):
    relic = models.ForeignKey(RelicWeapon, on_delete=models.CASCADE)
    step = models.IntegerField()
    quest_name = models.CharField(max_length=100)
    description = HTMLField()
    location = models.CharField(max_length=100)
    reward = models.ForeignKey("relics.Reward", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.quest_name

    class Meta:
        ordering = ['step']


class Reward(models.Model):
    reward_name = models.CharField(max_length=100)
    description = HTMLField()
    icon = models.ImageField(
        upload_to='relics/',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.reward_name
