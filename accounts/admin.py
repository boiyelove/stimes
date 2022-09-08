from django.contrib import admin
from .models import UProfile, USchoolProfile
# , EmailConfirmed, UserDefaultAddress, UserAddress
# from .models import Profile
# from django.contrib.auth.models import User
# # Register your models here.

# class UserProfileInline(admin.StackedInline):
# 	model = Profile

# class UserAdmin(admin.ModelAdmin):
# 	inlines = [UserProfileInline]

# admin.site.register(UserProfileInline)
admin.site.register(UProfile)
admin.site.register(USchoolProfile)
# admin.site.register(EmailConfirmed)
# admin.site.register(UserDefaultAddress)
# admin.site.register(UserAddress)