#blog/forms.py
from django import forms

from .models import Comment

class CommentsForm(forms.ModelForm):

    class Meta:

        model=Comment

        fields=('CommentTitle','CommentContent')