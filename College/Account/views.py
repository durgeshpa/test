from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


#from django.core import urlresolvers



def signup_view(request):
	message=None
	if request.method=='POST':
		form = SignUpForm(request.POST)
	
		if form.is_valid() and not User.objects.filter(email__iexact= form.cleaned_data.get('email')):
	
		
			user = form.save()
		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			if user and user.is_active :
				login(request, user)
				#print('hello')
				return redirect(('Account:home'))
		else:
			message='user name or email allready exists'
			form = SignUpForm()
			return render(request, 'account/resistration.html',{'form':form,'message':message})
	else:
		
		form = SignUpForm()

	return render(request, 'account/resistration.html',{'form':form,'message':message})
def signin_view(request,templates='account/login.html'):
	if request.method=="POST":
		data=request.POST.copy()
		user_name=data.get('username','')
		pass_word=data.get('password','')
		user = authenticate(username=user_name, password=pass_word,backend='django.contrib.auth.backends.ModelBackend')
		if user and user.is_active :
			login(request, user)
			#url = reverse('Accounts:home')
			return redirect(('Account:home'))
		else :
			return render(request,templates,{'message':'user does not exists'})

	else:
		return render(request,templates)
@login_required
def home(request,templates = 'account/home.html'):
	user_id = request.user
	print(user_id.first_name)

	return render(request,templates,{'user_id':user_id})

def logout_view(request):
	logout(request)
	return redirect(('Account:login'))
@login_required
def profile(request):
	if request.method == 'POST':
			#u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
			#if if  u_form.is_valid() and p_form.is_valid():					
			if  p_form.is_valid():
				#u_form.save()
				p_form.save()
			#messages.success(request, f'Your account has been updated!')
				return redirect(('Account:home'))

	else:
		print(request.user)
		#u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		#'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'account/home.html', context)
