from django import forms
from . models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'avatar',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords don't match")
        return password1

    def clean_email(self):
        email = self.cleaned_data['email']
        email = User.objects.filter(email=email).exists()
        if email:
            raise ValidationError("email already exists")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you van change the password <a href=\"../password/\"><h1>here</h1>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'avatar', 'password', 'last_login')

