from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from tryTen import settings

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Group(models.Model):
	TOPIC_CHOICES = (
		('fresh', 'fresh'),
		('cool', 'cool'),
		('nice','nice'),
	)


	title = models.CharField(max_length=200,choices = TOPIC_CHOICES, null=True)
	slug = models.SlugField(max_length=200 )
	category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('forum:forum_list', args=[self.slug])

class Event(models.Model):
	title = models.CharField(max_length=200, null=True)
	slug = models.SlugField(max_length=200 )
	image = models.ImageField(upload_to='event_images/', blank=True,null=True)
	description = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title