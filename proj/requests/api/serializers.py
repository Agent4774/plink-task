from rest_framework import serializers
from requests.models import Request
import string


class RequestSerializer(serializers.ModelSerializer):
		class Meta:
				model = Request
				fields = ('email', 'password', 'first_name', 'last_name')
				extra_kwargs = {'password': {'write_only': True}}

		def validate_email(self, email):
				if len(email) > 100:
						raise forms.ValidationError('Email must have no more than 100 symbols')
				if 'gmail.com' in email or 'icloud.com' in email:
						message = 'Domains gmail.com and icloud.com are not allowed'
						raise forms.ValidationError(message)
				return email

		def validate_password(self, password):
				if len(password) < 7 or len(password) > 16:
						raise forms.ValidationError('Password must have from 7 to 16 symbols')
				if not password[0].isupper():
						raise forms.ValidationError('Password must start with upper case letter')
				allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_'
				for char in password:
						if char not in allowed_chars:
								raise forms.ValidationError('Letters, digits and underscore allowed only')
				return password

		def validate_first_name(self, first_name):
				allowed_chars = string.ascii_uppercase + string.ascii_lowercase + '-'
				for char in first_name:
						if char not in allowed_chars:
								raise forms.ValidationError(f'Letters and hyphen allowed only')
				return first_name

		def validate_last_name(self, last_name):
				allowed_chars = string.ascii_uppercase + string.ascii_lowercase + '-' + ' '
				for char in last_name:
						if char not in allowed_chars:
								raise forms.ValidationError('Letters, hyphen and space allowed only')
				return last_name