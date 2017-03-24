from django import forms
from .models import Stock1
from django.contrib.auth.models import User
from .models import UserProfile

class StockForm(forms.ModelForm):
  class Meta:

      model=Stock1
      fields=['data','desc']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # labels = {
        #     'username': 'Unique service no',

        # }

class LoginForm(forms.ModelForm):
  class Meta:

      model=User
      fields=['email','password']

class UserProfileForm(forms.ModelForm):
    # phone_no = forms.CharField(widget=forms.)         need to complete it

    class Meta:
        model = UserProfile
        fields = ('adhar_no',)