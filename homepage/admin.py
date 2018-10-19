from django.contrib import admin
from .models import Message, Category, TrainingNote, ExpeditionReport

admin.site.register(Message)
admin.site.register(Category)
admin.site.register(TrainingNote)
admin.site.register(ExpeditionReport)