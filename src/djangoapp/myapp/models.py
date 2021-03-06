from django.db import models
# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    telnum = models.IntegerField(null=True)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomModel(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_url = models.URLField()
    room_token = models.CharField(max_length=120)
    image1_name = models.CharField(null=True, max_length=100)
    image1_path = models.ImageField(null=True, blank=True)
    image1_votenum = models.IntegerField(default=0)
    image2_name = models.CharField(null=True, max_length=100)
    image2_path = models.ImageField(null=True, blank=True)
    image2_votenum = models.IntegerField(default=0)

    def __str__(self):
        return self.room_name