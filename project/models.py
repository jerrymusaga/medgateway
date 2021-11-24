from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    topic = models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, blank=True, related_name='like')

    def __str__(self):
        return self.topic
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Question(models.Model):
    question = models.CharField(max_length=400)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


