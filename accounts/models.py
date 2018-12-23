from django.db import models
#from products.models import Purchase
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone

import re

from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
#from model_utils import Choices


class User(AbstractBaseUser, PermissionsMixin):

	class Meta:
		app_label = 'accounts'
		db_table = "user"
		#ordering=["created"]

	username = models.CharField(_('username'), max_length=75, unique=True,
		help_text=_('Required. 30 characters or fewer. Letters, numbers and '
					'@/./+/-/_ characters'),
		validators=[
			validators.RegexValidator(re.compile('^[\w.@+-]+$'), 
			_('Enter a valid username.'), 'invalid')
		])
	full_name = models.CharField(_('full name'), max_length=254, blank=True)
	last_name = models.CharField(_('short name'), max_length=30, blank=True)
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	
	def get_full_name(self):
		return self.full_name

	def get_last_name(self):
		return self.last_name

	def __unicode__(self):
		return self.email

	
	#USER_TYPES = Choices('investor', 'issuer_sponsor', 
	#'service_provider','broker_dealer')
	#user_type = models.CharField(choices=USER_TYPES, max_length=50)