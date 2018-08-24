from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    vemail = forms.EmailField(label='Verify your email here!')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        vmail = all_clean_data['vemail']

        if email != vmail:
            raise forms.ValidationError("You must enter the same email twice!")

