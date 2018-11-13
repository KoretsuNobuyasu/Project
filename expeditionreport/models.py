import os
from django.db import models
from django.utils import timezone

class Expeditionreport(models.Model):
    """海外遠征報告書"""

    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    file = models.FileField('ファイル', upload_to='files/', null=True, blank=True)
    created_at = models.DateTimeField('提出日', default=timezone.now)

    def get_filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.title

