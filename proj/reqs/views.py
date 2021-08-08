from .forms import RequestForm
from .models import Request
from .utils import get_request_ip
from django.http import HttpResponse
from django.shortcuts import render


def save_request(request):
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.ip = get_request_ip(request)
			instance.save()
			return render(request, 'reqs/save_request.html', {
				'form': form,
				'message': 'Request has been saved!'
			})
	else:
		form = RequestForm()
	return render(request, 'reqs/save_request.html', {
			'form': form
		})

def get_filtered_requests(request):
	reqs = Request.objects.filter(
		ip=get_request_ip(request)
	)
	if reqs.exists():
		return render(request, 'reqs/filtered_requests.html', {'reqs': reqs})
	return render(request, 'reqs/filtered_requests.html', {'message': 'No requests found'})