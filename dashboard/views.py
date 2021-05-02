from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboard.models import resource_entry
# Create your views here.

def home_page(request):

	resource_entries = resource_entry.objects.all().order_by('-added_on')
	return render(request,'homepage.html',{'entries' : resource_entries})
