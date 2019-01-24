from django.db import models

# Create your models here.


class Vtuber(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    belong = models.CharField(max_length=30)
    twiiter = models.CharField(max_length=30)
    channel_id = models.CharField(max_length=60)
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Youtuber(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    belong = models.CharField(max_length=30)
    twiiter = models.CharField(max_length=40)
    channel_id = models.CharField(max_length=60)
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.name
