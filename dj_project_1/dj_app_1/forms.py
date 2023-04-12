from django import forms
from dj_app_1.models import User

class NewUserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'