from django import forms

from .models import Comment

class CommentFrom(forms.modelform):
    class Meta:
        model = Comment
        fields = ['name','email','body']
