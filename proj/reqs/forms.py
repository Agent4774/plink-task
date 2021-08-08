from django import forms
from .models import Request
import string


class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ('email', 'password', 'first_name', 'last_name')

	def clean_email(self):
		email = self.cleaned_data['email']
		if len(email) > 100:
			raise forms.ValidationError('Email must have no more than 100 symbols')
		if 'gmail.com' in email or 'icloud.com' in email:
			message = 'Domains gmail.com and icloud.com are not allowed'
			raise forms.ValidationError(message)
		return email

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) < 7 or len(password) > 16:
			raise forms.ValidationError('Password must have from 7 to 16 symbols')
		if not password[0].isupper():
			raise forms.ValidationError('Password must start with upper case letter')
		allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_'
		for char in password:
			if char not in allowed_chars:
				raise forms.ValidationError('Letters, digits and underscore allowed only')
		return password

	def clean_first_name(self):
		first_name = self.cleaned_data['first_name']
		allowed_chars = string.ascii_uppercase + string.ascii_lowercase + '-'
		for char in first_name:
			if char not in allowed_chars:
				raise forms.ValidationError(f'Letters and hyphen allowed only')
		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data['last_name']
		allowed_chars = string.ascii_uppercase + string.ascii_lowercase + '-' + ' '
		for char in last_name:
			if char not in allowed_chars:
				raise forms.ValidationError('Letters, hyphen and space allowed only')
		return last_name