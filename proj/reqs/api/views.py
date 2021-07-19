from .serializers import RequestSerializer
from reqs.models import Request
from reqs.utils import get_request_ip
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RequestCreateAPIView(CreateAPIView):
		queryset = Request.objects.all()
		serializer_class = RequestSerializer
		permission_classes = [IsAuthenticated]

		def perform_create(self, serializer):
				serializer.save(ip=get_request_ip(self.request))
				

class FilteredRequestsAPIView(APIView):
		queryset = Request.objects.all()
		permission_classes = [IsAuthenticated]

		def get(self, request, *args, **kwargs):
				reqs = Request.objects.filter(
					ip=get_request_ip(request)
				)
				data = []
				for req in reqs:
						data.append({
							'email': req.email,
							'ip': req.ip,
							'first_name': req.first_name,
							'last_name': req.last_name
						})
				return Response(data)