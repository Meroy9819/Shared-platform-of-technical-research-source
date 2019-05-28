from django import forms
#from captcha.fields import CaptchaField


class SciAchiForm(forms.Form):
    create_name=forms.CharField(label="成果名称",max_length=512,widget=forms.TextInput(attrs={'class':'form-control'}))
    create_author=forms.CharField(label="作者",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    create_keywordSeq=forms.CharField(label="关键词序列",max_length=256,widget=forms.TextInput(attrs={'class':'form-control'}))
    create_refCount=forms.IntegerField(label="引用数",widget=forms.TextInput(attrs={'class':'form-control'}))
    create_publishyear=forms.CharField(label="发表年份",max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}))
    create_abstract=forms.CharField(label="摘要",max_length=1024,widget=forms.TextInput(attrs={'class':'form-control'}))

