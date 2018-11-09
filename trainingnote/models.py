from django.db import models
from django.utils import timezone


class TrainingNote(models.Model):
    """練習ノート"""

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('提出日',default=timezone.now)


class Comment(models.Model):
    """trainingnoteのコメンt"""

    name = models.CharField('コメント者',max_length=30, default="コーチ")
    text = models.TextField('本文')
    trainingnote = models.ForeignKey(TrainingNote, verbose_name='紐づく投稿', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
