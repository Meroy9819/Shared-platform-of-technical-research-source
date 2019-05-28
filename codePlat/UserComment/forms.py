
from django import forms

class CommentForm(forms.Form):
    CommentTitle = forms.CharField(label="评论标题",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    CommentContent = forms.CharField(label="评论内容", max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))