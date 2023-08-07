# forms.py
from django import forms

class LoginForm(forms.Form):
    print(forms)
    email = forms.CharField(label="email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
