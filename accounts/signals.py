import random
import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import EmailConfirmed

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
		# if not created:
		# 	return
		# user = instance
		# email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
		# if email_is_created:
		# 	base, domain = str(user.email).split("@")
		# 	activation_key = create_shorthash(base)
		# 	email_confirmed.activation_key = activation_key
		# 	email_confirmed.save()
		# 	# email_confirmed.activate_user_email()
		# profile = User.objects.create(user=instance)
		pass


def create_shorthash(a=""):
	if a:
		shorthash = hashlib.sha224(str.encode(str(random.random()))).hexdigest()[:10]
		shorthash = shorthash + str(a)
		shorthash = hashlib.sha224(str.encode(str(shorthash))).hexdigest()[:10]
	else:
		shorthash = hashlib.sha224(str.encode(str(random.random()))).hexdigest()[:10]
	return shorthash

