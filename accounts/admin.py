from django.contrib import admin

from .models import User

class userAdmin(admin.ModelAdmin):
	class Meta:
		model = User
admin.site.register(User, userAdmin)
