from django.conf.urls import url 
from django.urls import path

from . import views

app_name = 'feedback' 
urlpatterns = [
path('feedback_form', views.feedback_form, name='feedback_form'),
]
