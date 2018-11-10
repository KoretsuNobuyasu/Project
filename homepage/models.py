from django.db import models
from django.utils import timezone

class Menu(models.Model):
    """メニュー"""

    name = models.CharField('メニュー名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    """お知らせ"""

    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('掲示日', default=timezone.now)
    menu = models.ForeignKey(Menu, verbose_name='メニュー', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """コメント"""

    name = models.CharField('名前', max_length=30, default='監督orコーチ')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, verbose_name='紐づく練習ノート', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
