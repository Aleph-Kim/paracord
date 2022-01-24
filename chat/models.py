from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    reg_date = models.DateTimeField('채팅방 생성 날짜', auto_now_add=True)
    name = models.CharField('채팅방 이름', max_length=100, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    part_user = models.ManyToManyField(User, related_name="part_server")

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    writer = models.CharField('작성자', max_length=20)
    message = models.TextField('메시지 내용')
    timestamp = models.DateTimeField('메시지 전송 시간', auto_now_add=True)
