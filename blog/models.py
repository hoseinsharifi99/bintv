from django.contrib.admin.templatetags.admin_list import admin_actions
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    sumRate = models.IntegerField()
    sumVote = models.IntegerField()

    def __str__(self):
        return self.title

    def average_rating(self):
        if self.sumVote > 0:
            return float(self.sumRate / self.sumVote)
        return 0

    def ratings_count(self):
        return self.sumVote

class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.post.title} - {self.score}"
