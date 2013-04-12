from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from btp.forms import *

# Create your views here.

def register_page(request):
	if request.method == 'POST':
		print(request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
			)
			return HttpResponse(simplejson.dumps(""), mimetype='application/json')
			