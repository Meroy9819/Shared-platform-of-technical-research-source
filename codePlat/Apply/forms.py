from django import forms
class ApplyForm(forms.Form):
    apply_name=forms.CharField(label="真实姓名", max_length=512, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apply_institution=forms.CharField(label="所在机构", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apply_resource = forms.CharField(label="发表文章题目", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apply_resourceyear=forms.CharField(label="发表文章年份", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apply_field = forms.CharField(label="研究领域", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apply_photo=forms.ImageField(label="个人手持身份证正面照", widget=forms.ImageField(attrs={'class': 'form-control'}))


class VerificationForm(forms.Form):
    verification_image=forms.ImageField(label="个人手持身份证正面照", widget=forms.ImageField(attrs={'class': 'form-control'}))