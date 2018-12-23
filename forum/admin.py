from django.contrib import admin
from .models import Group, Category, Event

admin.site.register(Group)

admin.site.register(Category)

class EventAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug','date']
	prepopulated_fields = {'slug':('title',)}
admin.site.register(Event, EventAdmin)

