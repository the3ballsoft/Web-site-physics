from django import forms
from profiles.models import User

from materiales.models import  Material



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateMaterial(forms.ModelForm):


	class Meta:
		model = Material
		fields = ('titulo', 'descripcion', 'arichivo','curso')