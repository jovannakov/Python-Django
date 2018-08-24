import os

# set the environment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

from django.shortcuts import render
from . import forms
from Application.models import User

def index(request):
    return render(request, 'FirstApp/index.html')



def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            user = User.objects.get_or_create(name=name, email=email, text=text)[0]
            user.save()
            print("VALIDATION SUCCESS!")
            print("Name:", name)
            print("E-mail:", email)
            print("Text:", text)
    return render(request, 'FirstApp/FirstForm.html', {'form': form})
