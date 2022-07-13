from django.db import models


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    video = models.URLField()


class SubTopic(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.URLField()
    video = models.URLField()


class Word(models.Model):
    title = models.CharField(max_length=255)
    sub_topic = models.ForeignKey(SubTopic, on_delete=models.CASCADE)
    image = models.URLField()
    video = models.URLField()
