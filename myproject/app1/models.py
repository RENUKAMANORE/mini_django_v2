from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    another_field = models.CharField(
        max_length=250,
        choices=[("profile", "tester"), ("profile2", "developer")],
        default="DEFAULT"
    )

    def publish(self):
        self.publish_date = timezone.now
        self.save()

    def __str__(self):
       return self.title

class RandomTable(models.Model):
    username = models.CharField(max_length=250)
    questions = models.CharField(max_length=250)
    answer = models.TextField()





