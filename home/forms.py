__author__ = 'ali'

from django import forms
from django.utils.translation import ugettext as _

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': _('تفاصيل الخبر لا يزيد عن 300 حرف'),
               'cols': '60', 'rows': '3', 'required': 'required', 'maxlength':'300',
               'title': _('يجب كتابة تفاصيل الخبر')}))
    tags = forms.CharField(required=True, label=_('الأقسام (Tags)'), widget=forms.TextInput(
        attrs={'class': 'form-control col-sm-7', 'placeholder': _('افصل بين الاقسام بفاصلة'),
               'required': 'required', 'title': _('يجب كتابة التصنيف')}))

    class Meta:
        model = Post
        fields = ['content', 'tags']
        exclude = ('user', )
