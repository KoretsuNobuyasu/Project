from django.db import models,IntegrityError
from django.utils import timezone



class TrainingNote(models.Model):
    """練習ノート"""

    title = models.CharField('タイトル',max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('提出日',default=timezone.now)


class Comment(models.Model):
    """練習ノートへのコメント"""

    name = models.CharField('名前', max_length=30, default='名無し')
    text = models.TextField('本文')
    post = models.ForeignKey(TrainingNote, verbose_name='紐づく記事', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
