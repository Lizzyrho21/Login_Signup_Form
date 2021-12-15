
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this

# For our homepage
def homepage(request):
	return render(request, 'home.html')


#For signing the user up
def register_request(request):
    # Returns a Boolean value. If the form is used for user submissions..
	if request.method == "POST":
		form = NewUserForm(request.POST) # A form bound to the POST data
		if form.is_valid(): #If ALL form validation checks return to TRUE
			user = form.save() # save the form and assign it to user 
			login(request, user) # logs the user in
			messages.success(request, "Registration successful." )
			return redirect("main:homepage") #redirect to url route 'home'
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})