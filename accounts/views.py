__author__ = 'ali'

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm, ProfileForm


def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    context = {'title': 'تسجيل الدخول'}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            redirect_to = request.POST.get('next')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if len(redirect_to.strip()) > 0:
                        return redirect(redirect_to)
                    return redirect('home')
                else:
                    error = _('تم ايقاف الحساب من قبل الإدارة')
                    context['form'] = form
                    context['error'] = error
                    return render(request, 'accounts/login.html', context)
            else:
                error = _('أسم المستخدم/كلمة المرور غير صحيحة')
                context['form'] = form
                context['error'] = error
                return render(request, 'accounts/login.html', context)

    form = LoginForm()

    context = {'form': form, 'title': _('تسجيل الدخول')}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.user.is_authenticated():
        return redirect('home')

    context = {'title': _('تسجيل حساب جديد')}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password2'))
            auth.login(request, user)
            return redirect('home')
        else:
            context['form'] = form
            return render(request, 'accounts/register.html', context)
    form = RegisterForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)


@login_required()
def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['password1'] and form.cleaned_data['password2']:
                user.set_password(form.cleaned_data['password2'])
            user.save()

        context = {'title': _('تعديل البيانات'), 'req_user': request.user, 'form': form}
        return render(request, 'accounts/profile.html', context)

    form = ProfileForm(instance=user)
    context = {'title': _('تعديل البيانات'), 'req_user': request.user, 'form': form}
    return render(request, 'accounts/profile.html', context)
