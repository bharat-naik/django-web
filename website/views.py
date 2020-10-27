from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Message


# Views  Started




#home page view -index
def index(request):
	return render(request, 'website/index.html')



# register page view
def register(request):
        if request.method == "GET":
            return render(
            request, "website/register.html",
            {"form": UserCreationForm}
        )
        elif request.method == "POST":
        	form = UserCreationForm(request.POST)
        	if form.is_valid():
        	   user = form.save()
        	   login(request, user)
        	   return redirect(reverse("index"))
        	   
        	   


#chat page view

def chat(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			username=request.user.username
			msg=request.POST.get('message')
			c=Message(nm=username , txt=msg)
			c.save()
			mg=reversed(Message.objects.all())
			context={'amg':mg}
			return render(request, 'website/chat.html' ,context)
	
		else:
			username=request.user.username
			mg=reversed(Message.objects.all())
			context={ 'amg':mg}
			return render(request, 'website/chat.html' ,context)
		
	else:
		return render(request, 'website/log.html')
		
				
