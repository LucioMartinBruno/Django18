from django import forms

from .models import SignUp
from .models import Post

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email=forms.EmailField()
	message = forms.CharField()


class PostForm(forms.ModelForm):
	"""docstring for ClassName"""
	class Meta:
		model = Post
		fields= ["title","author"]
		
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["email","full_name"]
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")

		return full_name