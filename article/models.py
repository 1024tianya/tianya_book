from django.db import models
from django.contrib.auth.models import User
from user.models import Channel
# Create your models here.
import datetime


class Content(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=255, verbose_name='标题')
    text = models.TextField(verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length='50', verbose_name='标签')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论+回复
    """
    COMMENT, REPLY = ('评论', '回复')
    LEVEL_TYPE = (
        (0, "comments"),
        (1, "reply")
    )
    comments = models.TextField(verbose_name='评论内容',)
    contents = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='文章id')
    level = models.CharField(max_length=10, verbose_name='级别', choices=LEVEL_TYPE)
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户id')
    reply = models.TextField(verbose_name='回复', null=True, blank=True)
    like = models.IntegerField(max_length=10, verbose_name='点赞数量', null=True, blank=True)
    attention = models.BooleanField(default=False, verbose_name='关注')
    collection = models.BooleanField(default=False, verbose_name='收藏')
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.like


class InfoAttention(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    attention = models.BooleanField(default=False, verbose_name='关注')
    collection = models.BooleanField(default=False, verbose_name='收藏')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.attention


