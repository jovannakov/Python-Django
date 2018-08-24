from django.conf.urls import url
from Application import views

# TEMPLATE TAGGING

app_name = 'Application'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]