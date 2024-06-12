from apps import ticketSales
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProfileRegisterForm
from .models import ProfileModel

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect(reverse(ticketSales.views.timesInfo))
        else:
            context = {
                "user": username,
                "error": "کاربر با این نام یافت نشد..."
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', {})

def logoutView(request):
    logout(request)
    if request.GET.get("next"):
        return render(request.GET.get("next"))
    return redirect(reverse(ticketSales.views.concertListView))

@login_required
def profileView(request):
    profile=request.user.profile
    context={
        "profile":profile
    }
    return render(request,"accounts/profile.html",context)

def profileRegisterView(request):

    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(
                                username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=ProfileModel(user=user,
                                       ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                        Gender=profileRegisterForm.cleaned_data['Gender'],
                                        Credit=profileRegisterForm.cleaned_data['Credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        profileRegisterForm=ProfileRegisterForm()

  
    context={
        "formData":profileRegisterForm
    }


    return render(request,"accounts/profileRegister.html",context)
