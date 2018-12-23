from django.contrib import admin

from .models import Post,Tag, Comment

class PostAdmin(admin.ModelAdmin):
	class Meta:
		model = Post
	list_display = ("title", "created")
	prepopulated_fields = {"slug":("title",)}
admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
	class Meta:
		model = Tag
admin.site.register(Tag, TagAdmin)

admin.site.register(Comment)


