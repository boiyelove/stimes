from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from cities_light.models import Country
# Create your models here.
# class BaseProfile(models.Model):
# 	usertype = (
# 				(0, 'Student'),
# 				(1, 'Lecturer'),
# 				(2, 'Other'),
# 				)
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
# 	user_type = models.IntegerField(max_length=1, choices=usertype, null=True)
# 	bio = models.CharField(max_length=200, null = True, blank=True)

# 	def __str__(self):
# 		return self.user

# 	class Meta:
# 		abstract =True

# class LecturerProfile(models.Model):
# 	pass
class UProfile(models.Model):
	user = models.OneToOneField(User)
	country = models.ForeignKey(Country, related_name='user_country',null = True, blank=True)	
	bio = models.CharField(max_length = 240, null = True, blank=True)


class USchoolProfile(models.Model):
	school_name = models.CharField(max_length=50)
	school_ancronym = models.CharField(max_length=15,null = True, blank=True)
	country = models.ForeignKey(Country, related_name='user_scountry',null = True, blank=True)
	State = models.CharField(max_length = 60)
	Address = models.CharField(max_length = 200, blank = True, null = True)
	faculty = models.CharField(max_length=50, blank = True, null = True)
	department = models.CharField(max_length=50, blank=True, null =True)
	begin = models.DateTimeField()
	end = models.DateTimeField()



# class Profile(StudentProfile, LecturerProfile):
# 	pass


class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.confirmed)

	def activate_user_email(self):
		# activation_url = "%s%s" %(settings.SITEURL, reverse("activation_view", args=[self.activation_key]))
		# context = {
		# 	"activation_key" : self.activation_key,
		# 	"activation_url" : activation_url,
		# 	"user": self.user.username,
		# }
		# message = render_to_string("accounts/activation_message.txt", context)
		# subject = "Activate your Email"
		# return self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
		pass

	def email_user(self, subject, message, from_email=None, **kwargs):
		# return send_mail(subject, message, from_email, [self.user.email], kwargs)
		pass

# class UserDefaultAddress(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	shipping = models.ForeignKey("UserAddress", null=True, blank = True, related_name="user_address_shipping_default")
# 	billing = models.ForeignKey("UserAddress", null = True, blank = True, related_name="user_address_billin_default")

# 	def __str__(self):
# 		return str(self.user.username)

# class UserAddressManager(models.Manager):
# 	def get_billing_addresses(self, user):
# 		return  super(UserAddressManager, self).filter(billing=True).filter(user=user)

# class UserAddress(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL)
# 	address = models.CharField(max_length=120)
# 	address2 = models.CharField(max_length=120, null=True, blank=True)
# 	city = models.CharField(max_length=120)
# 	state = models.CharField(max_length=120)
# 	country = models.CharField(max_length=120)
# 	zipcode = models.PositiveSmallIntegerField()
# 	phone = models.PositiveIntegerField()
# 	shipping = models.BooleanField(default=True)
# 	billing = models.BooleanField(default = False)
# 	timestamp = models.DateTimeField(auto_now_add = False, auto_now= True)
# 	updated = models.DateTimeField(auto_now_add = True, auto_now= False)

# 	def __str__(self):
# 		return self.get_address()

# 	def get_address(self):
# 		return "%s, %s, %s, %s, %s" %(self.address, self.city, self.state, self, country, self.zipcode)

# 	objects = UserAddressManager()

# 	class Meta:
# 		ordering = ['-updated', 'timestamp']


class Message(models.Model):
	msender = models.ForeignKey(User, related_name = 'msender')
	content = models.TextField()
	mreceiver = models.ForeignKey(User, related_name = 'mreceiver')
	date_sent = models.DateTimeField()
	date_received = models.DateTimeField()