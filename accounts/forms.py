import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import UProfile, USchoolProfile

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
class RegisterForm(forms.Form):
	username = forms.CharField(label='Username', max_length=64)
	email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password', widget=forms.PasswordInput())

	# def clean_password(self):
	# 	cleaned_data = super(RegisterForm, self).clean()
	# 	username = cleaned_data.get("username")
	# 	password = cleaned_data.get("password")
	# 	if username == password:
	# 		return password		
	# 	raise forms.ValidationError("Your password shouldn't be the same as your username")

	def clean_username(self):
		cleaned_data = super(RegisterForm, self).clean()
		username = cleaned_data.get('username')
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('Username can only contain a-z, 0-9 and underscore _')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken, try another')

	def clean_email(self):
		cleaned_data = super(RegisterForm, self).clean()
		email = cleaned_data.get('email')
		try:
			User.objects.get(email = email)
		except ObjectDoesNotExist:
			return email
		raise forms.ValidationError('Email address already exist, please login instead')



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		try:
			user = User.objects.get(username=username)
		except ObjectDoesNotExist:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Invalid Password")
		elif user is None:
			pass
		else:
			return password


class UProfileForm(forms.ModelForm):
	class Meta:
		model = UProfile
		exclude = ['user']

class USchoolProfileForm(forms.Form):
	school_name = forms.CharField(max_length=50)
	school_ancronym = forms.CharField(max_length=15)
	country = forms.CharField(max_length = 30)
	State = forms.CharField(max_length = 60)
	Address = forms.CharField(max_length = 200)
	faculty = forms.CharField(max_length=50)
	department = forms.CharField(max_length=50)
	begin = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	end = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

	def clean(self):
		cleaned_data = super(USchoolProfileForm, self).clean()
		begin = cleaned_data.get("begin")
		end = cleaned_data.get("end")

