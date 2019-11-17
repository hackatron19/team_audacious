from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from.forms import UserRegisterForm
from.forms1 import Counselors
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.views.generic.edit import FormView
from django.contrib.auth.models import User,auth
from .forms import SampleForm



def index(request):
    return render(request, 'index.html', {'title': 'index'})

def home(request):
    return render(request, 'home.html', {'title': 'home'})




def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')

			htmly = get_template('email.html')
			d = {'username': username}
			subject, from_email, to = 'welcome', 'anubhabit687@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text / html")
			msg.send()

			messages.success(request, 'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form, 'title': 'register here'})


def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form': form, 'title': 'log in'})


def signup(request):
	return render(request, 'signup.html')

def register1(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')

			htmly = get_template('email.html')
			d = {'username': username}
			subject, from_email, to = 'welcome', 'anubhabit687@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text / html")
			msg.send()

			messages.success(request, 'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'register1.html', {'form': form, 'title': 'register here'})



class SampleView(FormView):

    form_class = SampleForm
    template_name = 'sample.html'