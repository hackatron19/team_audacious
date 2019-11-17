from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetimepicker.helpers import js_loader_url
from datetimepicker.widgets import DateTimePicker



Q_CHOICES = [
    ('B', 'Btech'),
    ('C6', 'school(class 6-10 )'),
    ('C10', 'school(class10-12)'),
    ('M', 'Mtech'),
    ('B', 'Bsc'),
    ]
class Counselors(UserCreationForm):
    email = forms.EmailField()
    Qualification = forms.CharField(label='Currently pursuing', widget=forms.Select(choices=Q_CHOICES))
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    contact = forms.IntegerField()