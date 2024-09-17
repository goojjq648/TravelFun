from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class MemberRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='密碼')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼')

    class Meta:
        model = Member
        fields = ['username', 'full_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密碼不匹配")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

from django import forms




class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'full_name', 'email', 'level', 'is_active', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ['username', 'full_name', 'email', 'password']

    def clean_password(self):
        return self.cleaned_data['password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }