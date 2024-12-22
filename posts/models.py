from django.db import models

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    userId = models.IntegerField()
    body = models.TextField()

    def __str__(self):
        return self.title
