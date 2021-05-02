from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboard.models import resource_entry
from django.db.models import Count
# Create your views here.

def home_page(request):

	resource_entries = resource_entry.objects.all().order_by('-added_on')
	cities = resource_entry.objects.values('city').annotate(dcount=Count('city'))
	resource_counts = resource_entry.objects.values('resource').annotate(dcount=Count('resource')).order_by('-dcount')[0:3]
	message = "Displaying data for all cities all resources."
	return render(request,'homepage.html',{'entries' : resource_entries,'cities':cities,'city':'All','resource':'All','resource_counts':resource_counts})


def submit_filter(request):

	if (request.method != 'POST'):
		return redirect('/')

	else:

		city_name = request.POST['city']
		resource_name = request.POST['resource']
		print(city_name)
		print(resource_name)
		entries = resource_entry.objects.filter(city=city_name,resource=resource_name)

		cities = resource_entry.objects.values('city').annotate(dcount=Count('city'))
		resource_counts = resource_entry.objects.values('resource').annotate(dcount=Count('resource')).order_by('-dcount')[0:3]
		
		return render(request,'homepage.html',{'entries' : entries,'cities':cities ,'city':city_name,'resource':resource_name,'resource_counts':resource_counts})

