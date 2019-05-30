
from django import forms

class CommentForm(forms.Form):
    CommentContent = forms.CharField(label="评论内容", max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))
