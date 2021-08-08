from .serializers import UserSerializer
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


User = get_user_model()
# JWT methods
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserCreateAPIView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserLoginAPIView(APIView):
	def post(self, request, *args, **kwargs):
		email = request.data.get('email')
		password = request.data.get('password')
		queryset = User.objects.filter(email=email)
		if queryset.exists():
			user = queryset.first()
			if user.check_password(password):
				login(request, user)
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				response = jwt_response_payload_handler(token, user, request)
				return Response(response)
		return Response(
			{'detail': 'Invalid credentials.'}, 
			status=status.HTTP_400_BAD_REQUEST
		)