from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from tryTen import settings


class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug


class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)


class Post(models.Model):
	STATUS_CHOISES = (
		('draft', 'Draft'),
		('published', 'Published')
	#	('teaser', 'Teaser')
	#	('important','Important')
	#	('latest', 'Latest')
	)

	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
	content = models.TextField()
	image = models.ImageField(upload_to='images/', blank=True,null=True)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='draft')
	modified = models.DateTimeField(auto_now=True)
	tags = models.ManyToManyField(Tag)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]

	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.id, self.slug])


class Comment(models.Model):
	Post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content = models.TextField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}-{}'.format(self.product.name, str(self.user.username))