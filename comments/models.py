from django.db import models
from django.contrib.auth.models import User
from project.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user.username)

