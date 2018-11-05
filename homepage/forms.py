from django import forms
from .models import Comment, Message_comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text')


class Message_commentCreateForm(forms.ModelForm):

    class Meta:
        model = Message_comment
        fields = ('name', 'text')