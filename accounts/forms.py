from django import forms
from django.contrib.auth import get_user_model

non_allowed_usernames = ["user"]

User = get_user_model()

class  LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username_iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid username.")
        return username


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label= 'Password', 
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'id': "user-password"}
        )
    )
    password2 = forms.CharField(
        label= 'Confirm Password', 
        widget= forms.PasswordInput(
            attrs={'class': 'form-control', 'id': "user-conf-password"}
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username_iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("You cannot use this username. Please pick another.")
        if not qs.exists():
            raise forms.ValidationError("You cannot use this username. Please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email_iexact=email)
        if not qs.exists():
            raise forms.ValidationError("There is already user with this email. Please pick another.")
        return email

#    def clean(self):
#        username = self.cleaned_data('username')
#        password = self.cleaned_data('password')

   
#iexact