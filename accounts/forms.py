__author__ = 'ali'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label=_('اسم المستخدم'),
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'اسم المستخدم',
                                                             'required': 'required',
                                                             'title': _('يجب كتابة اسم المستخدم')}))
    password = forms.CharField(label='كلمة المرور',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': _('كلمة المرور'),
                                                                 'required': 'required',
                                                                 'title': _('يجب كتابة كلمة المرور')}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label=_('اسم المستخدم'),
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'أسم المستخدم',
                                                             'required': 'required',
                                                             'title': _('يجب كتابة اسم المستخدم')}))
    password1 = forms.CharField(label='كلمة المرور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('كلمة المرور'),
                                                                  'required': 'required',
                                                                  'title': _('يجب كتابة كلمة المرور')}))
    password2 = forms.CharField(label='تأكيد كلمة المرور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('تأكيد كلمة المرور'),
                                                                  'required': 'required',
                                                                  'title': _('يجب تأكيد كلمة المرور')}))
    email = forms.CharField(label=_('البريد الالكتروني'),
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder': _('البريد الالكتروني'),
                                                           'required': 'required',
                                                           'title': _('يجب كتابة البريد الالكتروني')
                                                           }))
    first_name = forms.CharField(label=_('الأسم الاول'),
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': _('الأسم الاول'),
                                                               'required': 'required',
                                                               'title': _('يجب كتابة الأسم الاول')}))
    last_name = forms.CharField(label=_('أسم العائلة'),
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': _('أسم العائلة'),
                                                              'required': 'required',
                                                              'title': _('يجب كتابة أسم العائلة')}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=_('الأسم الاول'),
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': _('الأسم الاول'),
                                                               'required': 'required',
                                                               'title': _('يجب كتابة الأسم الاول')}))
    last_name = forms.CharField(label=_('أسم العائلة'),
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': _('أسم العائلة'),
                                                              'required': 'required',
                                                              'title': _('يجب كتابة أسم العائلة')}))
    email = forms.CharField(label=_('البريد الالكتروني'),
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder': _('البريد الالكتروني'),
                                                           'required': 'required',
                                                           'title': _('يجب كتابة البريد الالكتروني')
                                                           }))
    password1 = forms.CharField(label='كلمة المرور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('كلمة المرور'),
                                                                  'title': _('يجب كتابة كلمة المرور')}),
                                required=False)
    password2 = forms.CharField(label='تأكيد كلمة المرور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('تأكيد كلمة المرور'),
                                                                  'title': _('يجب تأكيد كلمة المرور')}),
                                required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('كلمة المرور غير متطابقة'))
        return password2

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2' )

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if self.clean_password2():
            user.set_password(self.clean_password2())
        if commit:
            user.save()
        return user
