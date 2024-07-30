from django.contrib import admin

from .models import UserProfile
class userprofileadmin(admin.ModelAdmin):
    list_display=('user','email')



# Register your models here.
admin.site.register(UserProfile, userprofileadmin)
