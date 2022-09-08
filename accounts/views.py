import re
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm, LoginForm, UProfileForm, USchoolProfileForm

# Create your views here.
# class ArticleUpdate(UpdateView):
#     model = Author
#     fields = ['name']
#     template_name_suffix = '_update_form'


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password'],
				email = form.cleaned_data['email']
				)
			return HttpResponseRedirect('/')
	else:
		form = RegisterForm()
	context = {'form':form}
	template = 'registration/registration_form.html'
	return render(request, template, context)

SHAI_RE =re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA_RE.search(activation_key):
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			messages.success(request, "There was an error with your request")
			return HttpResponseRedirect("/")
		if instance is not None and not instance.confirmed:
			page_message = "Confirmation Successful! Welcome."
			instance.confirmed = True
			instance.activation_key = "Confirmed"
			instance.save()
			messages.success(request, "Successsfully Confirmed Please Login")
		elif instance is not None and instance.confirmed:
			page_message = "Already Confirmed!, Please Login"
		else:
			page_message = ""

		context = {"page_message": page_message}
		return render (request, "account/activation_complete.html", context)
	else:
		raise Http404

def email_confirmed(request):
	pass

def login(request):
	form = LoginForm(request.POST or None)
	btn = 'Login'
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		message.success(request, "Successfully Logged In. Welcome Back!")
		return HttpResponseRedirect("/")
	context = {
		"form": form,
		"submit_btn" : btn,
	}
	return render(request, "registration/login.html", context)


def logout(request):
	logout(request)
	pass
def change_password(request):
	pass
def user_profile(request):
	Uform = UProfileForm(request.POST or None)
	Sform = USchoolProfileForm(request.POST or None)
	context = {'Uform' : Uform,
				'Sform': Sform,
				}
	template = 'accounts/profileform.html'
	return render(request, template, context)
