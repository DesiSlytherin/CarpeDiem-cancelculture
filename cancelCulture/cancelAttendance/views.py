from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def home_view(request):
	name = request.user.get_full_name()
	print(name)
	if request.user.is_superuser:
		data = leavereq.objects.filter(Status='Pending')
	else:
		data = leavereq.objects.filter(Name__contains=name)

	print(data)
	context = {}
	return render(request, 'student.html',{'data':data,})

@login_required(login_url='/login')
def form_view(request):
	form = leavereqForm()
	if request.method == "POST":
		print('hello')
		form = leavereqForm(request.POST,request.FILES)
		if form.is_valid():
			print('hello')
			form.save()
			return redirect('data')
		else:
			form = leavereqForm()
			return render(request,'second.html',{"form":form})

	return render(request,'second.html',{"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print(username+password)
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('data')
		else:
			form = AuthenticationForm()
			return render(request=request, template_name="index.html", context={"form":form})
	form = AuthenticationForm()
	return render(request=request, template_name="index.html", context={"form":form})

@login_required(login_url='/login')
def approve_view(request,objid):
	leavereq.objects.filter(id=objid).update(Status='Approved')
	return redirect('data')
@login_required(login_url='/login')
def reject_view(request,objid):
	leavereq.objects.filter(id=objid).update(Status='Rejected')
	return redirect('data')