from django.db import models

# Create your models here.


class Vtuber(models.Model):
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)
    belong = models.CharField(max_length=20)
    channel_id = models.CharField(max_length=40)
    youtube_url = models.CharField(max_length=80)
    tag1 = models.CharField(max_length=20)

    def __str__(self):
        return self.name1
