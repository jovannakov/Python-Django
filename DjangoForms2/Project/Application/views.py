from django.shortcuts import render
# from Application.models import User

from Application.forms import NewUserForm

# Create your views here.

def index(request):
       return render(request, 'FirstApp/index.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid!')
    return render(request, 'FirstApp/form.html', {'form': form})