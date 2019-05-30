from django import forms
#from captcha.fields import CaptchaField
class ReportForm(forms.Form):
    error = (
        ('title', '标题错误'),
        ('author', '作者错误'),
        ('keyword', '关键词错误'),
        ('year', '发表年份错误'),
        ('abstract', '摘要错误'),
        ('author', '作者错误'),
        ('sciAchiUrl', '论文文件错误')
    )
    ReportContent = forms.CharField(label="举报内容说明详情", max_length=6000, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Reporttype = forms.ChoiceField(label='错误类型', choices=error)
 #   captcha = CaptchaField(label='验证码')


class ReportFormExpert(forms.Form):
    error = (
        ('name', '姓名错误'),
        ('institution', '所在机构错误'),
        ('paper_number', '论文发表数量错误'),
        ('H_index', 'H指数'),
        ('G_index', 'G指数'),
        ('field', '领域错误'),
    )
    ReportContent = forms.CharField(label="举报内容说明详情", max_length=6000,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    Reporttype = forms.ChoiceField(label='错误类型', choices=error)
#   captcha = CaptchaField(label='验证码')