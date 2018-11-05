from django.contrib import admin
from .models import Message, Category, TrainingNote, ExpeditionReport, Menu, Comment, Message_comment

admin.site.register(Message)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(TrainingNote)
#admin.site.register(ExpeditionReport)
admin.site.register(Comment)
#admin.site.register(Message_comment)