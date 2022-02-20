from django.shortcuts import render
from .models import Contacts
# Create your views here.


def index(request):
	if request.method=="POST":
		print(save)
		Contacts.objects.create(
			yourname=request.POST['yourname'],
	        youremail=request.POST['youremail'],
	        subject=request.POST['subject'],
	        message=request.POST['message'],
			)
		msg="Massage Has Been Saved Successfully............"
		return render(request,'index.html',{'msg':msg})
	else:
		print("index")
		return render(request,'index.html')

def innerpage(request):
	return render(request,'inner-page.html')

def portfoliodetails(request):
	return render(request,'portfoliodetails.html')






