from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	content = forms.CharField(required=True , widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder':'Write your comment here'
		}
		))
	class Meta:
		model = Comment
		fields = ('content',)
		