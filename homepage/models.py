from django.db import models
from django.utils import timezone


class Category(models.Model):
    """カテゴリ"""

    name = models.CharField('カテゴリ名',max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name

class Menu(models.Model):
    """メニュー"""

    name = models.CharField('メニュー名', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Message(models.Model):
    """お知らせ"""

    text = models.CharField('txt', max_length=255)
    news = models.TextField('本文')
    created_at = models.DateTimeField('掲示日', default=timezone.now)
    menu = models.ForeignKey(Menu, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.text

class TrainingNote(models.Model):
    """練習ノート"""

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('提出日',default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class ExpeditionReport(models.Model):
    """海外遠征報告書"""

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('提出日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title