from django import forms
from .models import Group

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ('title', 'slug', 'content')
