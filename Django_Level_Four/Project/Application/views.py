from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Application/index.html')

def other(request):
    return render(request, 'Application/other.html')

def relative(request):
    return render(request, 'Application/relative_url_templates.html')

