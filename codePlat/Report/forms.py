from django import forms
#from captcha.fields import CaptchaField
class ReportForm(forms.Form):
    ReportContent = forms.CharField(label="举报内容说明详情", max_length=6000, widget=forms.TextInput(attrs={'class': 'form-control'}))
 #   captcha = CaptchaField(label='验证码')