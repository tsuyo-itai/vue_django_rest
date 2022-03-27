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

    def __str__(self):
        return self.room_name