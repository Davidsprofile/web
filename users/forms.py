from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    username = forms.CharField(
        label='Username',
        required=True,
        help_text='Not allowed: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Enter Password',
        required=True,
        help_text='Password should not be easy to guess',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Email'})
    )
    username = forms.CharField(
        label='Username',
        required=True,
        help_text='Not allowed: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Upload Image',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
