from django import forms
from Application.models import User


class NewUserForm (forms.ModelForm):
    verifyPw = forms.CharField(max_length=20)
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'
