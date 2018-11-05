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


class Comment(models.Model):
        """コメント(監督・コーチのみアクセス可能) / 基本的には練習ノートにのみコメントされ、海外遠征報告書には連絡なし"""

        name = models.CharField('名前',max_length=30, default='監督orコーチ')
        text = models.TextField('本文')
        trainingnote = models.ForeignKey(TrainingNote, verbose_name="紐づく練習ノート", on_delete=models.PROTECT)
        created_at = models.DateTimeField('作成日', default=timezone.now)


        def __str__(self):
            return self.text[:10]


class Message_comment(models.Model):
        """メッセージに対するコメント(基本的に登録者であれば誰でもコメント可能)"""

        name = models.CharField('名前', max_length=30, default='名前を入力してください。')
        text = models.TextField('本文')
        message = models.ForeignKey(Message, verbose_name="紐づくお知らせ",on_delete=models.PROTECT)
        created_at = models.DateTimeField('作成日', default=timezone.now)

        def __str__(self):
            return self.text[:10]
