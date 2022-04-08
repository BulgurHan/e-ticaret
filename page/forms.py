from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Adınız'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Soyadınız'
        })
    )
    username = forms.CharField(
        max_length = 100,
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kullanıcı Adınız'
        })
    )
    email = forms.EmailField(
        max_length=254,
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ör.  adınız@örnek.com'
        })
    )
    password1 = forms.CharField(
    max_length = 100,
    required=True,
    widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parola'
        })
    )
    password2 = forms.CharField(
    max_length = 100,
    required=True,
    widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolanızı Doğrulayın'
        })
    )

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','username', 'password1', 'password2')




class SignInForm(forms.Form):

    username = forms.CharField(
        max_length = 100,
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Kullanıcı Adınız'
        })
    )
    password = forms.CharField(
    max_length = 100,
    required=True,
    widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parola'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password')